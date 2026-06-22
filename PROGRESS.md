# PROGRESS.md — Learning Tracker

> Single source of truth for "where am I." Claude Code reads `CLAUDE.md`, which sends it here.
> Keep entries short and dated. Update after every passed gate and at the end of each session.

## Current status

- **Phase:** 3 — IaC & CI/CD
- **Active module:** G1 — GitHub Actions *(IN PROGRESS — all teaching done; gate NOT yet taken)*
- **Last verified:** T1 — Terraform for WAF ✅ (passed 2026-06-21)

## ▶ Next action

**Resume G1 at the KNOWLEDGE GATE** (learner paused right before answering; all 5 concepts taught,
pipeline built & proven working live). Ask these 5, grade honestly, then mark G1 passed + update
checklist/log:
1. Why `pull_request` (pre-merge gate) over checks on `push` to `main` (post-merge)?
2. Why is OIDC safer than a stored access key? (two reasons: no long-lived secret at rest +
   short expiry; cryptographically scoped to the repo via the `sub` claim)
3. What does `permissions: id-token: write` do, and what breaks without it? (no OIDC token minted)
4. What attack does the trust-policy `sub: repo:jhukdk/python-tutor-for-boto3awswaf:*` prevent?
   (another repo's token assuming the role)
5. Why did CI `plan` say `1 to add` for an existing resource, and the fix? (local state not shared
   with CI → remote S3 backend).

After the gate passes → **G1 done = Phase 3 complete.** Open item: **PR #3 is mergeable (CI green)**
— offer to merge + branch cleanup. Then Phase 4 / S1 (detection & response). Also still-open
enhancements (now in README "In progress"): remote Terraform state (S3 backend) and a gated
post-merge `apply` job.

---

## Module checklist

### Phase 0 — Python fundamentals
- [x] M1 — Variables, types, printing, f-strings  *(2026-06-17)*
- [x] M2 — Lists  *(2026-06-17)*
- [x] M3 — Loops  *(2026-06-18)*
- [x] M4 — Conditionals  *(2026-06-18)*
- [x] M5 — Dictionaries  *(2026-06-18)*
- [x] M6 — Nested data structures  *(2026-06-19)*
- [x] M7 — Functions  *(2026-06-19)*
- [x] M8 — JSON & error handling  *(2026-06-19)*
- [x] **Phase 0 exit gate** — parse a response-shaped dict: loop, filter, pull nested fields,
      summarize via f-string, inside a function with try/except  *(2026-06-20)*

### Phase 1 — Boto3 core
- [x] B1 — Clients, sessions, regions  *(2026-06-20)*
- [x] B2 — Calls & reading responses  *(2026-06-20)*
- [x] B3 — Pagination  *(2026-06-21)*
- [x] B4 — Boto3 error handling (ClientError)  *(2026-06-21)*

### Phase 2 — AWS WAF
- [x] W1 — Concepts (Web ACL, rules, rule groups, IP sets, scope)  *(2026-06-21)*
- [x] W2 — Read-only inventory  *(2026-06-21)*
- [x] W3 — Analysis (sampled requests, logging, CloudWatch metrics)  *(2026-06-21)*
- [x] W4 — Controlled changes (owner-authorized writes)  *(2026-06-21)*

### Phase 3 — IaC & CI/CD
- [x] T1 — Terraform for WAF  *(2026-06-21)*
- [ ] G1 — GitHub Actions (OIDC to AWS, Terraform CI)

### Phase 4 — Security engineering & interview readiness
- [ ] S1 — Detection & response / rule tuning
- [ ] I1 — Interview prep (scenarios, design, live Boto3 coding)

---

## Session log

- **2026-06-17** — Environment verified (Boto3 1.43.32). Completed M1: types, f-strings,
  `5` vs `"5"`, and a fix for an unterminated-string `SyntaxError`. Passed M1 gate (3/4 clean,
  the 4th a typo over correct understanding). Introduced M2 (Lists); gate still open.
- **2026-06-17** — Passed M2 (Lists): zero-based indexing, `len()`, `[-1]`, `.append()`,
  and `IndexError`. Predicted every snippet correctly and aced the gate task with no hints;
  articulated the count-vs-index gap clearly. Created `fundamentals/m02_lists.py`. Next: M3 (Loops).
- **2026-06-18** — Passed M3 (Loops): `for` over a list, `range()`, reading a nested loop,
  and building a list with `.append()` inside a loop. Predicted every output correctly (incl.
  nested-loop ordering) and explained the loop variable. Created `fundamentals/m03_loops.py`.
  Next: M4 (Conditionals).
- **2026-06-18** — Passed M4 (Conditionals): `if`/`elif`/`else`, comparison operators
  (`==`, `!=`, `<`, `>`), boolean operators (`and`/`or`/`not`), and the loop+`if` filter
  pattern. Predicted every snippet correctly, spotted the `=` vs `==` bug (and that it's a
  `SyntaxError`), and wrote filter loops cleanly with no hints. Next: M5 (Dictionaries).
- **2026-06-18** — Passed M5 (Dictionaries): create/access by key, `["key"]` `KeyError` vs
  `.get()` returning `None`/fallback, and iterating `.keys()`/`.values()`/`.items()` (incl.
  two-variable unpacking). Predicted all output correctly (incl. a list-valued field) and
  explained strict-vs-soft access cleanly. Created `fundamentals/m05_dicts.py`. Next: M6.
- **2026-06-19** — Passed M6 (Nested data structures): list-of-dicts access, dict-holding-
  list-of-dicts, deep chaining (`response["WebACLs"][0]["Rules"][0]["Action"]`), and loop+
  filter over nested lists. Needed one hint to assemble the first loop+filter; everything
  after (incl. 3-level gate) was clean and correct. Created `fundamentals/m06_nested.py`.
  Note: learner on Python 3.12+ (nested same-quote f-strings run); still coached the
  single-quote-inside habit for portability. Next: M7 (Functions).
- **2026-06-19** — Passed M7 (Functions): `def` with parameters, `return` vs implicit `None`
  (`NoneType`), and default arguments (overridden positionally and by keyword). Aced all four
  gate questions with no hints — predicted f-string defaults, nailed the implicit-`None` recall,
  wrote `count_rules` with `len()` cleanly, and explained the maintainability/drift argument for
  functions in security tooling. Created `fundamentals/m07_functions.py`. Next: M8 (JSON & errors).
- **2026-06-19** — Passed M8 (JSON & error handling): `json.dumps` (dict→string), `json.loads`
  (string→dict), `indent=` for readability, `try`/`except`, and specific-vs-bare `except`.
  Partial on first pass — two small gaps: thought plain `dumps` (no `indent=`) pretty-prints
  (it's compact single-line), and left an `except` body empty. Both closed cleanly on re-check.
  Created `fundamentals/m08_json.py`. Next: Phase 0 exit gate (capstone).
- **2026-06-20** — Passed the **Phase 0 exit gate** on a fresh variant (learner asked for an
  extra capstone rep before Phase 1). Wrote `summarize_regional(response)` over an IP-set-shaped
  dict: looped, filtered `Scope == "REGIONAL"`, pulled `len(Addresses)`, f-string summary, all
  inside a function with a specific `except KeyError`. Clean, no hints. Coaching only (no impact
  on pass): nested same-quote f-string (`f"{num["Name"]}"`) runs on 3.12+ but reinforced the
  single-quote-inside habit for portability; cosmetic format difference; suggested domain-shaped
  var names (`ipset` over `num`) for readable tooling. **Phase 0 complete.** Next: B1 (Boto3
  clients/sessions/regions) — read-only per guardrails.

- **2026-06-20** — Passed **B1 (Clients, sessions, regions)**: created `boto3.client("wafv2",
  region_name=...)`, explained the credential chain (named env vars / `~/.aws/` files / SSO-role),
  and the region-vs-`Scope` two-dial model. Aced all 4 gate questions; predicted client region
  for CloudFront (`us-east-1`) twice unprompted. Reinforced: credential chain is *ordered*
  (env → shared files → role/SSO, first match wins); and the cleaner scope rule (REGIONAL → the
  resource's region; CLOUDFRONT → always `us-east-1`) since the one-sentence answer didn't carry
  the CloudFront exception. Created `boto3_core/b1_client.py`. Next: B2 (calls & responses).
- **2026-06-20** — Passed **B2 (Calls & reading responses)**: made first live read-only call
  (`list_web_acls`), distinguished the data key (`WebACLs`) from `ResponseMetadata`/`NextMarker`,
  and looped the list-of-dicts to print each `Name`. Aced all 3 gate questions. **Real-world
  win:** an ACL "missing" from the REGIONAL listing turned out to be CLOUDFRONT-scoped — learner
  debugged it live, cementing the scope/region "two drawers" model (empty list ≠ no resources;
  often wrong scope/region). Coaching: redundant `if acl["Name"]:` guard (doesn't prevent
  KeyError — `[]` always fetches; use `.get()` for a real presence check); `[]` for AWS-guaranteed
  fields (Name) vs `.get()` for optional ones (Description); domain var names (`acl` not `num`).
  Created `boto3_core/b2_list_acls.py`. Next: B3 (pagination).
- **2026-06-21** — Passed **B3 (Pagination)**. **Key discovery:** WAFv2 ships an *empty*
  paginators file (`{"pagination": {}}`) — NO wafv2 op has a paginator; `get_paginator` raises
  `OperationNotPageableError`. So B3 pivoted from the happy-path paginator to the **manual
  `NextMarker` `while` loop**, which is the real pattern for this learner's whole domain.
  Introduced the **`while` loop** as a new Python concept (condition checked first → 0 runs when
  one page; fetch-first-page-then-loop pattern; `"key" in dict` membership; list `+` concat).
  Learner initially said one page → loop runs once (corrected to **0**: condition false up front),
  then traced 1-page/2-page cases correctly. Gate: 1 & 3 solid; sharpened #2 ("not pageable" =
  no paginator object, NOT that data never pages → still must handle NextMarker manually) and #4
  (the #1 infinite-loop cause is a *code bug* — forgetting to feed NextMarker back / reassign
  response — not an outage; and silent incompleteness = the dangerous security failure mode).
  Created `boto3_core/b3_paginate.py`. Next: B4 (ClientError handling).
- **2026-06-21** — Passed **B4 (Boto3 error handling)** — **Phase 1 complete.** Caught
  `botocore.exceptions.ClientError` (from `botocore`, not boto3) around a deliberately-failing
  read-only `get_web_acl` (fake Id → `WAFNonexistentItemException`), read the code at
  `e.response["Error"]["Code"]`, and branched with `if`/`elif`/`else` on codes
  (`WAFNonexistentItemException`/`AccessDeniedException`/`ExpiredTokenException`/else-raw).
  Predicted the not-found code unprompted. Bug: `IndentationError` (the `if` block indented
  deeper than `code =` — same-block statements must align); also flagged unused `f` prefix on
  non-interpolated strings. Gate clean; one phrasing correction — you distinguish error types by
  reading the `Code` *string at runtime*, not by inspecting botocore source. Cemented the
  expired-SSO playbook (not a code bug → `aws sso login`). Created `boto3_core/b4_errors.py`.
  Next: Phase 2 / W1 (WAF concepts).

- **2026-06-21** — Passed **W1 (WAF concepts)** — first Phase 2 module, vocabulary-only.
  Covered: Web ACL (rules in priority order + default action as safety net), rules (priority
  low-first, statement, action), the three actions (**Allow/Block terminating, Count
  non-terminating/observe-only**), rule groups + AWS Managed Rule Groups (Common/SQLi/
  KnownBadInputs/IpReputation) and per-rule Count override, IP sets (static known-bad,
  CIDR /32 vs /24, the most common future write op) vs rate-based rules (dynamic per-IP rate
  threshold), and scope/region (REGIONAL → resource's region; CLOUDFRONT → always us-east-1)
  plus WAFv2 (`"wafv2"`) vs deprecated Classic (`"waf"`). **Gate: 5/5, no hints** — nailed the
  Count-then-Block false-positive-triage workflow, the static-IP-set-vs-dynamic-rate distinction,
  and both scope dials. Strong conceptual grasp; tied back cleanly to the B2 "missing" CloudFront
  ACL. Next: W2 (read-only inventory — get_web_acl on the real ACL, list_rule_groups, IP sets).

- **2026-06-21** — Passed **W2 (Read-only inventory)**. Ran the real **list → get → loop**
  flow against the learner's own CloudFront ACL `jhuk-tech-cloudfront` (Scope=CLOUDFRONT,
  us-east-1): `list_web_acls` (summary only — no rules), then `get_web_acl` (Name+Id+Scope) →
  `response["WebACL"]` with `DefaultAction` `{'Allow': {}}` and 3 rules. Looped `web_acl["Rules"]`
  pulling Name/Priority/Action, using `rule.get("Action", rule.get("OverrideAction"))` to handle
  both authored rules and rule-group refs. **Real ACL shape uncovered:** [0] DemoBlockByHeader
  →Block (authored), [1] AWSManagedRulesCommonRuleSet →OverrideAction `{'None':{}}` (managed
  group, NOT overridden = live/blocking, contrast with `{'Count':{}}`), [2] RateLimitPerIP →Block
  (rate-based). Taught the nested-`.get()` fallback line in depth (fallback always evaluated).
  **Gate: 3/4 clean** (list-vs-get, the 3 get params, why `.get()` not `[]`→KeyError). Q4 bug:
  looped `for rule in web_acl:` (iterates dict **keys** → `rule["Priority"]` = TypeError on a
  str) instead of `web_acl["Rules"]` — the dict-is-not-its-contents gap; closed cleanly on
  re-check (predicted the Priority>=1 filter output correctly). Files: `waf/w2_list_acls.py`,
  `waf/w2_get_acl.py`. Next: W3 (analysis — sampled requests, logging, CloudWatch metrics).

- **2026-06-21** — Passed **W3 (Analysis)** — all three read-only lenses against the real
  `jhuk-tech-cloudfront` ACL. (1) **`get_sampled_requests`**: learned metric name ≠ rule name
  (pulled `RuleMetricName` from `rule["VisibilityConfig"]["MetricName"]` — e.g. DemoBlockByHeader
  → `jhuk-tech-demo-block-header`); hit a **real API correction live** — WAFv2 wants
  **`WebAclArn`** (full ARN from `response["WebACL"]["ARN"]`), NOT `WebAclId` (ParamValidationError);
  built a `TimeWindow` with new Python **`datetime.now(timezone.utc)` + `timedelta(hours=3)`**
  (≤3-hr, last-3-hr limit); got `0` (valid). Parsed a hardcoded SampledRequests dict
  (Request.ClientIP/Country/URI/Method + Action) — predicted output correctly. (2) **Logging**:
  `get_logging_configuration` → **logging is ON** to CloudWatch Logs group
  `aws-waf-logs-jhuk-tech-cloudfront` (taught mandatory `aws-waf-logs-` prefix; wrapped in B4-style
  `ClientError`/`WAFNonexistentItemException` handling). (3) **CloudWatch metrics**: separate
  **`cloudwatch`** client, `get_metric_statistics`, namespace **`AWS/WAFV2`**,
  Allowed/Blocked/**CountedRequests** per rule (the Count→Block tuning signal); got `[]` (valid).
  **Gate: 4/5 clean + a 5th closed on re-check** — Q4 conflated client (`cloudwatch`) with
  namespace (`AWS/WAFV2`); separated "service = door / namespace = drawer." Strong intuition that
  empty `0`/`[]` are valid not errors. Files: `waf/w3_sampled.py`, `waf/w3_parse_sample.py`,
  `waf/w3_logging.py`, `waf/w3_metrics.py`. Next: **W4 — controlled changes (mutating; guardrails).**

- **2026-06-21** — Passed **W4 (Controlled changes)** — **first mutating module; Phase 2
  complete.** **Guardrail change:** learner (sole owner of `jhuk-tech-cloudfront`, a low-traffic
  personal blog) explicitly authorized create/update/delete of IP sets & rules against it;
  CLAUDE.md updated with a dated, scoped "Sanctioned write target" block (kept confirm-before-
  write + blast-radius statement + get→modify→update(LockToken) as deliberate change-control
  habits). Ran a full real-write CRUD lifecycle on a CLOUDFRONT IP set `w4-practice` (seeded
  with reserved doc CIDRs 192.0.2.0/24, 198.51.100.0/24 → zero traffic impact, attached to
  nothing): **create_ip_set** (got LockToken), **update_ip_set** (taught the critical
  **replace-not-append** gotcha → GET current list, append, send full list), a deliberate
  **WAFOptimisticLockException** demo (reused a stale token → rejected, proving tokens rotate per
  write; recovery = re-GET/re-apply/retry), and **delete_ip_set** (also needs a fresh token; noted
  WAFAssociatedItemException if still referenced). **Gate: 3/5 clean, 2 closed on re-check** —
  #3 dropped the middle **MODIFY** step (framed it as "copy token"; the point of the pattern is
  read→change→write-whole), #5 gave mechanics not **security blast radius** (Count = observe-only
  → previously-blocked exploit patterns now reach the origin). Both nailed on re-ask. Files:
  `waf/w4_create_ipset.py`, `waf/w4_update_ipset.py`, `waf/w4_lock_demo.py`, `waf/w4_delete_ipset.py`.
  **Phase 2 / AWS WAF complete.** Next: Phase 3 / T1 (Terraform for WAF).

- **2026-06-21** — Passed **T1 (Terraform for WAF)** — first IaC module, new tool (Terraform
  v1.15.6 already installed; AWS provider v6.51.0). Taught **declarative vs imperative**
  (idempotence: 2nd apply = no-op), HCL **provider + resource** blocks (`aws_wafv2_ip_set`,
  type vs local name), and the full **`init → plan → apply`** loop. Ran it live: created a real
  CLOUDFRONT IP set **`tf-practice`** (`192.0.2.0/24`, us-east-1, attached to nothing → zero
  traffic impact) — the Terraform-managed twin of W4's hand-built `w4-practice`. Key tie-back:
  `lock_token` shows as `(known after apply)` and **Terraform manages the optimistic-lock token
  automatically** (the W4 get→modify→update dance is now the tool's job). Covered **state**
  (`terraform.tfstate` = TF's memory / config↔real-resource mapping) and **drift** (out-of-band
  Console/Boto3 edits surface in next plan → apply reverts to declared state = the security/audit
  win). Updated `.gitignore` (commit `.tf` + `.terraform.lock.hcl`; ignore `.tfstate`,
  `.terraform/`, `*.tfvars` — state holds secrets). **Gate: 4/5 clean** — only miss: thought
  `.terraform.lock.hcl` is "concurrency control"; corrected → it's the **provider-version
  dependency lock** (reproducible inits). Strong declarative intuition throughout (predicted
  idempotence and drift-revert unprompted). Files: `terraform/main.tf` (+ `.terraform.lock.hcl`).
  Learner chose to **keep** the live `tf-practice` IP set (Terraform-managed). Next: G1 (GitHub
  Actions — OIDC to AWS, Terraform CI).

- **2026-06-22** — **G1 (GitHub Actions) — IN PROGRESS, all teaching complete, paused before the
  knowledge gate.** Covered, one concept at a time: (1) **Actions model** — workflow/`on:` trigger/
  jobs/steps; chose `pull_request` as a PRE-MERGE gate (learner first guessed `push`-to-main;
  corrected via timeline — post-merge = too late; "shift left"). (2) **First workflow**
  `.github/workflows/terraform.yml` — `validate` job (checkout → setup-terraform → `fmt -check` →
  `init -backend=false` → `validate`), no AWS needed; explained `defaults.run.working-directory`
  (applies to `run:` not `uses:` steps). Merged as **PR #2** (green). (3) **OIDC concept** — why
  stored access keys are bad (long-lived secret at rest) vs OIDC (no secret at rest + ~1h expiry +
  repo-scoped trust); learner got the scoping half, coached the "no standing secret" half.
  (4) **AWS bootstrap built live (real IAM writes, owner-authorized):** OIDC identity provider for
  `token.actions.githubusercontent.com` ALREADY EXISTED (account `877995959706`) → reused its ARN;
  created IAM role **`github-actions-terraform-plan`** (role id `AROA4Y3FDEWNPQEIUEMPR`) with a
  trust policy scoped to `repo:jhukdk/python-tutor-for-boto3awswaf:*` + a least-privilege inline
  policy (`wafv2:GetIPSet`/`ListIPSets`/`ListTagsForResource`). Captured both policies as
  version-controlled files in `iam-bootstrap/`. (5) **Wired OIDC + plan** — added a `plan` job
  (`needs: validate`, `permissions: id-token: write`, `aws-actions/configure-aws-credentials@v4`
  with `role-to-assume: ${{ vars.AWS_ROLE_ARN }}`, `terraform plan`); set repo variable
  `AWS_ROLE_ARN` via `gh`. **PR #3** opened — first push DIDN'T trigger (path filter was
  `terraform/**` only; PR touched `.github/` + `iam-bootstrap/`) → real teaching moment; fixed by
  adding `.github/workflows/terraform.yml` to the `paths` filter. **Re-ran GREEN:** `validate ✓`
  + `plan ✓`; log shows `Authenticated as assumedRoleId AROA...:GitHubActions` (OIDC exchange
  worked, zero stored keys) and `Plan: 1 to add` (CI has empty local state → motivates remote
  state). Also updated README (IaC + CI/CD promoted to demonstrated capabilities) on the same PR.
  (Minor warning seen: Node20 deprecation on the pinned actions — future cleanup.) **PR #3 is
  mergeable; gate still owed.** Resume at the 5 gate questions in Next action.

## Stumbling blocks / things to revisit

- Watch for missing closing quotes/brackets in f-strings (caused a `SyntaxError` in M1).
- Reinforce zero-based indexing and the `IndexError` boundary as part of M2.
- (2026-06-19) Learner asked a sharp post-M6 question: do you hardcode `[0]` in real Boto3?
  Clarified the rule — **lists → loop, dicts → key, `[0]` only when "exactly one" is
  guaranteed.** Showed a real `list_web_acls` → `get_web_acl` flow with zero hardcoded
  indexes. Also flagged that my M6 example fused two real responses into one for teaching;
  revisit the true two-call shape when we reach Phase 1 (B2). Worth reinforcing in M7/Phase 1.

## Notes / cheatsheet

_(Add your own quick references here as you go.)_
