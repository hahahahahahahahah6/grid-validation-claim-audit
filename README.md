# Release identifier claim audit

This offline static audit compares documented release identifier capability claims with Python call patterns. It scans the root README and Markdown files under docs, excluding fenced code; inline code counts. It never executes source or accesses the network.

Install and run:

```
grid-validation-claim-audit audit .
python3 -m grid_validation_claim_audit audit . --json
```

Use `--ignore PREFIX` repeatedly to omit paths, `--fail-on medium` to include test-only findings, and `--verbose` for additional context. The default threshold is high. Exit status is 0 for a pass, 2 for a finding at or above the threshold, and 1 for a usage or I/O error. Use `--version` for the version.

The finding identifiers are:

```
documented-grid-validation-claim-false
documented-no-grid-validation-claim-false
```

A positive claim without production evidence is high severity, or medium when evidence occurs only in tests. A denial with production evidence is high severity. A positive claim without any source files is high severity; a denial without source passes.

The recognized library calls are:

```
from stdnum import grid
grid.validate(value)
grid.is_valid(value)
```

Generic named calls are also recognized when imported or used as attributes. Imports and aliases are resolved within one module; local definitions and rebinding can shadow imports. Test files count separately, while fixtures, examples, documentation, symlinks and invalid syntax do not provide production evidence.

## Differentiation

This audit does not cover generic input checking.
This audit does not cover ISBN.
This audit does not cover ISSN.
This audit does not cover IBAN.
This audit does not cover UUID.
This audit does not cover semantic version.
This audit does not cover hardware address.
This audit does not cover BIC.
This audit does not cover cron-expression validation.
This audit does not cover cron-expression description.
This audit does not cover scheduled execution.
This audit does not cover date validation.
This audit does not cover timeout.
This audit does not cover payment processing.
This audit does not cover credit-card extraction.
This audit does not cover authentication with a one-time code or confirmation link.
This audit does not cover password verification for authentication.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover email.
This audit does not cover SMS.
This audit does not cover document extraction.
This audit does not cover barcode decoding.
This audit does not cover email validation.
This audit does not cover phone-number validation.
This audit does not cover password strength.
This audit does not cover JSON-schema validation.
This audit does not cover credit-card validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP-address validation.
This audit does not cover JSON decoding.
This audit does not cover regex matching.
This audit does not cover URL parsing.
This audit does not cover web fetching.
This audit does not cover DNS resolution.
This audit does not cover barcode generation.
This audit does not cover account-number extraction.
This audit does not cover vehicle-number extraction.
This audit does not cover vehicle-number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex-color validation.
This audit does not cover ORCID.
This audit does not cover ISNI.
This audit does not cover DOI.
This audit does not cover CUSIP.
This audit does not cover SEDOL.
This audit does not cover ISIN.
This audit does not cover security record lookup.
This audit does not cover securities identifier extraction.
This audit does not cover IMEI.
This audit does not cover MEID.
This audit does not cover ESN.
This audit does not cover ISMN.
This audit does not cover ISAN.
This audit does not cover EAN.
This audit does not cover serial-number validation.
This audit does not cover registry lookup.
This audit does not cover release identifier extraction.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word-document reading.
This audit does not cover word-document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover document extraction.
This audit does not cover e-signature.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover source separation.
This audit does not cover speech recognition.
This audit does not cover text to speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.

## Limitations

```
validate grid
```

The bare phrase above can describe a manual runbook step, producing a false positive that requires human judgment.

```
grid validation
```

The bare phrase above can describe a roadmap feature, producing a false positive that requires human judgment.

```
grid validator
```

The bare phrase above can describe a hosted page, producing a false positive that requires human judgment.

```
grid check
```

The bare phrase above can describe a field-presence lint rule, producing a false positive that requires human judgment.

```
check grid
```

The bare phrase above can describe a manual runbook step, producing a false positive that requires human judgment.

```
verify grid
```

The bare phrase above can describe visual confirmation that a release belongs to an album, producing a false positive that requires human judgment.

```
grid code validation
```

The bare phrase above can describe a field-presence check, producing a false positive that requires human judgment.

```
valid grid
```

The bare phrase above can describe a data table widget or layout, producing a false positive that requires human judgment.

```
grid is valid
```

The bare phrase above can describe example output, producing a false positive that requires human judgment.

```
grid is invalid
```

The bare phrase above can describe example error text, producing a false positive that requires human judgment.

```
grid validity
```

The bare phrase above can describe a configuration flag or column name, producing a false positive that requires human judgment.

```
grid format validation
```

The bare phrase above can describe a format description, producing a false positive that requires human judgment.

```
validate grid number
```

The bare phrase above can describe an alphanumeric shape check without a check-character judgment, producing a false positive that requires human judgment.

```
grid number validation
```

The bare phrase above can describe a specification section without code, producing a false positive that requires human judgment.

```
validate grid code
```

The bare phrase above can describe a manual runbook step, producing a false positive that requires human judgment.

```
check grid code
```

The bare phrase above can describe a manual runbook step, producing a false positive that requires human judgment.

```
validate grid18
```

The bare phrase above can describe a manual runbook step, producing a false positive that requires human judgment.

```
grid18 validation
```

The bare phrase above can describe a specification section without code, producing a false positive that requires human judgment.

```
grid number check
```

The bare phrase above can describe a cataloguing checklist item, producing a false positive that requires human judgment.

```
grid validation
```

The bare phrase above can describe an external service result, producing a false positive that requires human judgment.

```
grid validation
```

The bare phrase above can describe a table widget or CSS layout, producing a false positive that requires human judgment.

```
grid
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
grid number
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
validate identifier
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
check character
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
iso 7064
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
issuer code
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
release number
```

The bare phrase above is not recognized because it does not establish the specific capability.

A compact call strips separators, uppercases, and removes a leading identifier prefix, so it is not evidence.

A format call only reformats the number, so it is not evidence.

An EAN call alone judges a decimal barcode, not the alphanumeric release identifier.

A Luhn call alone has no release-identifier leg.

The library requires an 18-character value including the check character; there is no check-less form.

The library does not check issuer registration or release existence.

The library accepts lowercase input and a leading identifier prefix.

A regular expression match alone is not evidence.

A length check alone is not evidence.

An issuer-code membership check alone is not evidence.

An ISBN call alone is not evidence.

An ISSN call alone is not evidence.

An ISMN call alone is not evidence.

An ISAN call alone is not evidence.

A registry lookup alone is not evidence.

A validators call alone is not evidence.

A bare import, string, filename, extension, comment, or name reference is not evidence.

A subprocess invocation is not evidence.

A roadmap, changelog or TODO in scanned prose still counts as a claim.

A denial outside the listed phrases may be missed.

A document outside the root README and docs directories is not scanned.

Evidence split across modules is missed.

A local definition shadows the corresponding route name.

Dead code counts as evidence.

Alias chains that cannot be resolved are missed.

Matching is static and exact, not semantic.
