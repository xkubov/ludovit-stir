# Ľudovít Štír

A convenient Slovak/Czech Translation Telegram Bot

Convenient but hloupy :(

## How to develop

This package uses [poetry](https://python-poetry.org). To install Nerd Assistant (and its dependencies), use:

```bash
$ poetry install
```

Then, you can start a virutualenv using `poetry shell`:

```bash
$ poetry shell
```

## Running

You can run the CLI app from `poetry shell`:

```bash
ludovit_stir
```

To see all the options use:

```bash
ludovit_stir --help
```

### Linting & Formatting

You can run linter & formatter from `poetry shell`:

```
$ poe lint
$ poe format
```

### Tests

You can run tests with the following command:

```bash
$ poetry run pytest
```

### Adding dependencies

To add runtime dependencies use:

```
$ poetry add $PACKAGE_NAME
```

To add development dependencies use:

```
$ poetry add --dev $PACKAGE_NAME
```

## Releasing new version

To create a release commit and tag use from `poetry shell`:

```
$ poe release (major|minor|patch)
```
