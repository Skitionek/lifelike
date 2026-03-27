# Copilot Instructions

- Always use Conventional Commits for every commit message.
- Use this format: `<type>(<optional-scope>): <description>`.
- Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- Keep the description short and imperative (for example: `fix(api): handle null user id`).
- Mark breaking changes with `!` after type/scope (for example: `feat(auth)!: remove legacy token flow`) and include `BREAKING CHANGE:` in the commit body when applicable.
