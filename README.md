# AWS WAF Automation & Analysis — Python + Boto3

A hands-on body of work demonstrating practical command of **AWS WAFv2** automation and traffic
analysis with **Python + Boto3**, built toward a **Perimeter Security Engineer** role. Every
exercise was planned then executed against live AWS infrastructure — from read-only inventory 
and log-based analysis to controlled, lock-safe changes on a production Web ACL. Progression 
is **knowledge-gated**: each module advances only after the underlying concepts
are demonstrated under examination by Claude Code, not merely read.

> **Stack:** AWS · Boto3 · Python 3 · CloudWatch — extending into Terraform & GitHub Actions.

---

## Demonstrated capabilities

### AWS WAF management & analysis
- **Inventory & configuration** — enumerate Web ACLs and resolve full configurations
  (`list_web_acls` → `get_web_acl`), parsing rules, priorities, and the `Action` vs
  `OverrideAction` distinction for managed rule groups.
- **Traffic analysis** — pull sampled requests (`get_sampled_requests`), inspect WAF logging
  configuration, and read CloudWatch metrics (`AWS/WAFV2`: Allowed / Blocked / CountedRequests
  per rule) to reason about what traffic a rule is actually catching.
- **Controlled changes** — full create → update → delete lifecycle on IP sets using the
  `get → modify → update(LockToken)` pattern, with correct handling of optimistic-lock
  conflicts (`WAFOptimisticLockException`) — executed safely against a production Web ACL.
- **Domain fluency** — Web ACLs, rule priority and terminating vs. observe-only (Count) actions,
  AWS Managed Rule Groups, IP sets, rate-based rules, and REGIONAL vs. CLOUDFRONT scope.

### Boto3 & AWS integration
- Client/session construction, the AWS credential chain, and the region-vs-`Scope` model
  (REGIONAL → resource's region; CLOUDFRONT → `us-east-1`).
- Reading and navigating API responses; manual `NextMarker` pagination where no paginator exists.
- Robust error handling via `botocore.exceptions.ClientError`, branching on the error `Code`.

### Python engineering foundations
Applied throughout in AWS-shaped contexts (response dicts, rule lists, nested structures):
core types & f-strings, lists, `for`/`while` loops, conditionals & filtering, dictionaries
(`["key"]` vs `.get()`), deeply nested data navigation, functions, and JSON + structured
exception handling.

---

## Repository layout

```
.
├── fundamentals/   # Python engineering foundations, one concept per file
├── boto3_core/     # Boto3 client, calls, pagination, error handling
├── waf/            # WAF inventory, traffic analysis, controlled changes
├── CLAUDE.md       # engagement instructions & AWS safety guardrails
└── PROGRESS.md     # detailed, dated work log
```

Each file is small, self-contained, and runnable on its own.

---

## Running the code

```bash
source .venv/bin/activate        # macOS / Linux  (.venv\Scripts\Activate.ps1 on Windows)

python waf/w2_list_acls.py       # e.g. enumerate Web ACLs
```

Boto3 inherits credentials from the authenticated AWS CLI via the standard credential chain —
**no keys are hardcoded anywhere in this repository.**

---

## Engineering & safety discipline

The work follows the guardrails in [`CLAUDE.md`](./CLAUDE.md) — the same change-control habits
expected on a production security team:

- **Read-only by default**; mutations only when explicitly intended and authorized.
- **Every write states its change and blast radius up front**, then proceeds on confirmation.
- **No hardcoded credentials** — credentials come from the inherited chain.
- **Scope and region made explicit** on every call (REGIONAL vs. CLOUDFRONT).
- **All writes use `get → modify → update(LockToken)`** and handle optimistic-lock conflicts.

---

## In progress

- **Infrastructure as Code** — modeling WAF resources in Terraform (`plan`/`apply`, state & drift).
- **CI/CD** — GitHub Actions validating and planning Terraform on pull requests, with OIDC auth
  to AWS (no long-lived keys).
- **Detection & response** — rule tuning from real sampled traffic, rate-based and bot controls,
  and false-positive triage.

See [`PROGRESS.md`](./PROGRESS.md) for the full, dated log.
