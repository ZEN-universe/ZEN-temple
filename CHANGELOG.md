## Changelog

## 0.7.4 (2025-10-15)

- Update import of ZEN-garden's `default_config` to new location.

## 0.7.3 (2025-10-02)

- Check whether corresponding scenario folders exist when loading solutions list.
- Skip model folders and show user-friendly error when loading results for a non-existing solution.
- [Nodal] Add duals to energy balance response.

## 0.7.2 (2025-09-22)

- [Nodal, Storage] Quantify timeseries data to reduce network bandwidth.

## 0.7.1 (2025-08-15)

- Pass `convert_to_yearly_unit=True` argument to `results.get_unit`.

## 0.7.0 (2025-08-15)

- Download multiple components at once for get_full_ts and get_total.
- Define number of significant digits in the CSV responses.

## 0.6.2 (2025-06-21)

- Fix no_open_browser option in CLI.
- Do not load import, export, and demand dataframes when loading solution detail.
- Fix #22 by removing unused components property from SolutionDetail.

## 0.6.1 (2025-05-28)

- Make package PEP 561 compliant.
- Add CLI argument to pass a file descriptor to the server process.

## 0.6.0 (2025-05-27)

- Change folder structure for a flat layout by moving `src/zen_temple` to `zen_temple`.
- Add script to automatically run `mypy` on every push to the server.
- Add CLI interface to ZEN temple

## 0.5.0 (2025-05-01)

- Update ZEN Explorer to v0.5.0.

## 0.4.3 (2025-04-03)

- Fix "years stay on x-axis".
- Fix scaleY labels that did not update.
- Load data for storage data all in parallel.
- Show correct unit.

## 0.4.2 (2025-04-02)

- Fix some errors regarding scenarios and simplify scenario settings such as carriers etc.
- Fix error if time series is empty.
- Fix that conversion to reference year happens twice.

## 0.4.0 (2025-03-12)

- Hide results that are numerically insignificant.
- Fix error in `get_full_ts` when there is no data.
- Update ZEN Explorer to v0.4.0
- Set correct version tag in `pyproject.toml`
