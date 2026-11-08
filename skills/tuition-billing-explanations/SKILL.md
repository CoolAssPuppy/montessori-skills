---
name: tuition-billing-explanations
description: Explain a tuition schedule or invoice line by line from the actual agreement, fee policy, and ledger. Use when a family asks what a charge means. For matching payments to bank or processor evidence, use payment-record-reconciliation. Do not mark an invoice paid without evidence or send without approval.
metadata:
  audience: "Admin"
---

# Explain a tuition invoice

Walk the family through the lines that already exist. Montessori books do not set fees.

## When to use

A family or office colleague needs to understand a schedule, invoice, or balance.

Matching bank/processor files: `payment-record-reconciliation`. Tone of a family email: `family-school-messages`.

## Inputs

- School, family account, period, currency
- Enrollment/tuition agreement
- Fee policy
- Invoice and ledger export
- Recorded payments and credits as they appear in those files

## Procedure

1. Confirm documents: title, version, invoice id, period.
2. Classify each line: recurring tuition, fee, deposit, credit, discount, recorded payment. Quote the policy clause for charges and due dates.
3. Recalculate quantity × unit price and the remaining balance. Show the arithmetic. Mark disputed or missing lines rather than guessing.
4. White: factual, respectful clarification; name the billing contact.
5. F1 (UK academy-trust management accounting guide, 23 Oct 2024) supplies control context for receivables: evidence, review, distinguish actual vs budget. It is England guidance. Local tax, chart of accounts, and collection law belong to the school's accountant.
6. FN reads: `billing_invoice_list` / `get` (administrator role). Sends: `billing_invoice_send` emails the parent and creates a notification; prose requires confirm. Create/pay/refund are separate mutations. `service_month` on tuition/club/meal lines must be `YYYY-MM-01`. See [references/integration.md](references/integration.md).

Do not mark paid without a payment record. Do not invent a waiver.

## Output

- Line table: description, period, amount, due date, source clause
- Payments applied
- Remaining balance
- Questions / missing evidence
- Unsent explanation draft
- Recalculation shown

## Adaptations

Plain language; translate if the school does. Keep legal terms from the agreement in quotes.

## Safeguards

See [references/records.md](references/records.md). No collection threats you did not find in policy.

## Sources and limits

See [references/evidence.md](references/evidence.md).
