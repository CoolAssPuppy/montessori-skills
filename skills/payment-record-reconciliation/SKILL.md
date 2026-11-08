---
name: payment-record-reconciliation
description: Compare school payment records with independent source evidence and list matches, unmatched entries, and timing differences. Use for bank, card, or processor reconciliation. For explaining an invoice to a family, use tuition-billing-explanations. Do not post journals, refunds, or settlements automatically.
metadata:
  audience: "Admin"
---

# Reconcile payments to independent evidence

Match records. Leave differences unmatched until a reviewer decides.

## When to use

The office has a school ledger and a bank, card, or processor export for the same period.

Family-facing explanation: `tuition-billing-explanations`.

## Inputs

- Period, currency, account scope
- School ledger export with ids
- Independent source (bank, Stripe, etc.)
- Opening and closing totals as stated on those files
- Reviewer name if known

## Procedure

1. Confirm the files are complete for the period. If a day is missing, stop and say so.
2. F1 §2: reconcile bank and cards; retain evidence; independent review. §§4-6: balance sheet, cash flow, debtors as context. This is England academy-trust guidance. A qualified local accountant owns statutory treatment in other jurisdictions.
3. Match on more than one field: amount, date, family id, invoice id, processor id. Show why each match holds.
4. Split **timing differences** (deposited next period) from **unmatched**.
5. Show opening total, plus matches, plus unmatched, toward the closing total. If it does not tie, say the unexplained remainder.
6. Proposed follow-up is a question list, not a posted journal. Do not net unrelated items to force a zero.
7. FN `billing_invoice_pay` records a payment and prose requires confirm. `refund`, `cancel`, bulk actions, and CSV export are separate. Do not call them to "finish" a recon ([references/integration.md](references/integration.md)).

Montessori texts have no authority for journals, tax, or collections. Treat ledger "paid" as a bookkeeping mark until bank or processor evidence matches.

## Output

- Worksheet: opening, matches, unmatched, timing, closing
- Evidence ids for each match
- Unexplained remainder
- Reviewer
- Proposed questions (no auto-post)

## Adaptations

If files use different timezones, state both.

## Safeguards

See [references/records.md](references/records.md). Synthetic fixtures in tests only.

## Sources and limits

See [references/evidence.md](references/evidence.md).
