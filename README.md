# Selenium Automation Framework Improvements

## Selector Strategy

- Primary: `[aria-label]` (accessibility)
- Fallbacks: `[data-testid]`, `[role]`, visible text (last resort)
- No absolute XPaths are used.
- All element location is centralized in `ElementFinder`.

## Configuration

- All environment-specific data (URLs, credentials) are externalized via environment variables.
- See `.env.example` for required variables.
- Backward compatibility: defaults are provided for local execution.

## Error Handling & Logging

- All waits and actions are wrapped with error handling and logging.
- Error messages include action, element name, page context, and current URL.

## Usage

- Tests use the `DashboardPage` class and `ElementFinder` utility.
- To run tests, set environment variables or use a `.env` loader.
