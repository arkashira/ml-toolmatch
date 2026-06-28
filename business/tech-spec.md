# tech‑spec.md – ml‑toolmatch (v1)

---

## 1. Stack (language / framework / runtime)

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **Backend language** | **Python 3.11** | Dominant in ML ecosystem, easy integration with existing datasets (auto, messages, conversations). |
| **Web framework** | **FastAPI** (async, OpenAPI auto‑gen) | Low latency, built‑in validation with Pydantic, excellent for micro‑service APIs. |
| **ORM / DB‑abstraction** | **SQLModel** (SQLAlchemy 2 + Pydantic) | Seamless mapping to PostgreSQL, type‑safe models, auto‑generated schemas. |
| **Task queue** | **Celery 5** + **Redis** broker | Background jobs for tool‑recommendation scoring, data refresh, email notifications. |
| **ML / recommendation** | **scikit‑learn** + **NumPy** | Light‑weight similarity / clustering models (e.g., TF‑IDF on tool descriptions, K‑NN). |
| **Runtime** | **Docker 24.x** (multi‑stage builds) | Portable, reproducible, aligns with Axentx CI/CD pipeline. |
| **API docs** | **Swagger UI** (via FastAPI) | Immediate developer feedback, useful for internal BD/PM consumption. |
| **Testing** | **pytest** + **httpx** (async client) | Unit + integration coverage > 80 %. |
| **Lint / type‑check** | **ruff** + **mypy** | Enforce code quality, fast CI feedback. |

---

## 2. Hosting (free‑tier‑first, specific platforms)

| Component | Provider | Free‑tier / Cost‑effective option | Deployment model |
|-----------|----------|-----------------------------------|------------------|
| **Container registry** | **GitHub Container Registry** | Unlimited public images, 500 MiB storage for private | Pull from CI to host |
| **Compute (API)** | **Render.com** (Web Service) | Free tier: 750 hrs/mo, 512 MiB RAM, 1 vCPU | Docker container, auto‑scaling |
| **Background workers** | **Render.com** (Background Worker) | Free tier: 750 hrs/mo, same limits | Runs Celery worker |
| **Cache / broker** | **Redis Labs** (Redis Cloud) | Free tier: 30 MiB, 1 GB‑hrs/mo | Used as Celery broker & result store |
| **Database** | **Supabase** (PostgreSQL) | Free tier: 500 MB, 2 GB‑hrs/mo, 500 M rows | Primary data store |
| **Static assets (frontend)** | **Vercel** (Next.js) | Free tier: 100 GB bandwidth, 125 k serverless invocations | Serves React UI |
| **Observability** | **Grafana Cloud** (Free) | 3 dashboards, 50 M series, 10 GB logs | Loki + Prometheus remote write |
| **Secrets management** | **Render.com** (Env vars) + **GitHub Actions Secrets** | No extra cost | Injected at build/run time |

*All services can be upgraded to paid plans without architectural changes.*

---

## 3. Data Model (tables / collections + key fields)

| Table (PostgreSQL) | Primary Key | Core Columns | Description |
|--------------------|-------------|--------------|-------------|
| **users** | `id` (UUID) | `email` (unique), `hashed_password`, `role` (`admin`, `bd`, `startup`), `created_at`, `last_login` | Authenticated accounts (internal BD + external startup users). |
| **startups** | `id` (UUID) | `name`, `stage` (`seed`, `Series A`, `Series B`), `team_size_ml`, `budget_range`, `industry`, `created_at` | Profile of the startup requesting advice. |
| **tools** | `id` (UUID) | `name`, `category` (e.g., “data‑labeling”, “experiment‑tracking”), `vendor`, `pricing_model`, `url`, `description`, `tags` (JSONB array), `created_at` | Master catalog of ML tooling (seeded from public sources + manual curation). |
| **recommendations** | `id` (UUID) | `startup_id` (FK), `tool_id` (FK), `score` (float), `rank` (int), `generated_at` | One‑to‑many mapping of a startup to ranked tool suggestions. |
| **feedback** | `id` (UUID) | `recommendation_id` (FK), `user_id` (FK), `rating` (1‑5), `comment`, `created_at` | Capture post‑recommendation user feedback for model retraining. |
| **audit_log** | `id` (UUID) | `user_id` (FK), `action`, `resource_type`, `resource_id`, `ip_address`, `timestamp` | Immutable trail for security/compliance. |

**Indexes**

* `users.email` – unique B‑tree.  
* `tools.category, tools.tags` – GIN on `tags` for fast tag filtering.  
* `recommendations.startup_id, recommendations.rank` – composite index for ordered retrieval.  

---

## 4. API Surface (5‑10 endpoints)

| Method | Path | Purpose | Request Body / Params | Response |
|--------|------|---------|-----------------------|----------|
| **POST** | `/api/v1/auth/login` | Issue JWT for a user | `{email, password}` | `{access_token, token_type:"bearer", expires_in}` |
| **POST** | `/api/v1/auth/register` | Register a new startup user | `{email, password, startup_id}` | `{user_id, email}` |
| **GET** | `/api/v1/startups/{startup_id}` | Retrieve startup profile (auth‑required) | – | Startup JSON |
| **POST** | `/api/v1/startups/{startup_id}/request` | Trigger recommendation generation (async) | `{team_size_ml, budget_range, industry, tags[]}` | `{job_id}` |
| **GET** | `/api/v1/recommendations/{job_id}` | Poll status / fetch results | – | `{status:"pending|ready|failed", results?:[Recommendation]}` |
| **GET** | `/api/v1/tools` | Browse catalog with filters | `?category=&tag=` | List of tools (paginated) |
| **POST** | `/api/v1/feedback` | Submit rating for a recommendation | `{recommendation_id, rating, comment}` | `{feedback_id}` |
| **GET** | `/api/v1/healthz` | Liveness / readiness probe | – | `{status:"ok"}` |
| **GET** | `/api/v1/openapi.json` | Auto‑generated OpenAPI spec | – | JSON schema |
| **GET** | `/api/v1/admin/audit` | (admin only) stream audit logs | `?limit=&offset=` | List of audit entries |

*All endpoints (except health) require a Bearer JWT with role‑based access control (RBAC).*

---

## 5. Security Model

| Aspect | Implementation |
|--------|----------------|
| **Authentication** | **OAuth2 Password Flow** with **JWT** signed by RS256 (private key stored in Render secrets). Token lifetime: 1 h + refresh token (7 days). |
| **Authorization** | **RBAC** via `role` claim (`admin`, `bd`, `startup`). FastAPI dependencies enforce per‑endpoint permissions. |
| **Password storage** | **argon2id** (via `passlib`) with per‑user salt. |
| **Secrets** | All keys (JWT private key, DB password, Redis password, third‑party API tokens) stored as **environment variables** in Render; never committed. |
| **Transport** | Enforced **HTTPS** (Render provides TLS termination). All internal service‑to‑service calls also over HTTPS. |
| **Input validation** | Pydantic models + FastAPI request validation; sanitise any free‑text before persisting. |
| **Rate limiting** | **Redis‑based token bucket** (max 60 req/min per IP for public endpoints). |
| **CORS** | Allow only `https://ml-toolmatch.com` and internal subdomains. |
| **Data protection** | GDPR‑compliant: `users` table includes `email` consent flag; ability to export/delete data via `/api/v1/users/me` endpoints (future). |
| **Audit** | Every mutating request logs to `audit_log` with user ID, action, IP, timestamp. |

---

## 6. Observability (logs, metrics, traces)

| Layer | Tool | What’s captured |
|-------|------|-----------------|
| **Application logs** | **Python `structlog` → Grafana Loki** (via fluent‑bit sidecar) | JSON logs: request_id, user_id, endpoint, latency, error stack. |
| **Metrics** | **Prometheus client** (exposed at `/metrics`) → Grafana Cloud | HTTP request count/status, latency histograms, Celery task duration, DB connection pool size. |
| **Tracing** | **OpenTelemetry** (Python SDK) → **Grafana Tempo** | End‑to‑end request trace across API → DB → Celery worker. |
| **Health checks** | `/healthz` endpoint + Render health probes | Liveness/readiness for auto‑restart. |
| **Alerting** | Grafana alerts (CPU > 80 % for 5 min, error rate > 2 %) → Slack webhook (internal Ops channel). |
| **Dashboards** | Pre‑built Grafana panels: request latency, recommendation job queue depth, user sign‑up funnel. |

All observability agents are configured via environment variables; no code changes needed for future scaling.

---

## 7. Build / CI

| Stage | Tool | Steps |
|-------|------|-------|
| **Source** | GitHub (repo `arkashira/ml-toolmatch`) | Branch protection: PR must pass CI, 2‑approver review. |
| **CI** | **GitHub Actions** | 1. `checkout` 2. `setup-python@v5` (3.11) 3. `pip install -r requirements.txt` 4. **Lint** (`ruff check .`) 5. **Type check** (`mypy .`) 6. **Unit tests** (`pytest -q --cov=app`) 7. **Build Docker image** (multi‑stage) 8. **Push** to GitHub Container Registry (if `main` branch). |
| **CD** | **Render.com** (auto‑deploy) | Render watches the container image tag; on new tag, it pulls and restarts API service + worker. |
| **Database migrations** | **Alembic** (integrated in CI) | `alembic upgrade head` executed in a Render “pre‑deploy” hook. |
| **Security scanning** | **Bandit** + **Safety** | Run after lint; fail CI on high‑severity findings. |
| **Performance regression** | **locust** (optional, nightly) | Simulated load of recommendation endpoint; alerts on > 30 % latency increase. |
| **Release tagging** | Semantic versioning (`vMAJOR.MINOR.PATCH`) | Automated via `semantic-release` on merge to `main`. |

*All secrets for CI (Docker registry token, DB credentials) are stored in GitHub Actions Secrets and injected as environment variables.*