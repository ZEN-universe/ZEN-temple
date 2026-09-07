# ZEN-temple

ZEN-temple is a FastAPI application that provides a REST API to access results from [ZEN-garden](https://github.com/ZEN-universe/ZEN-garden). It is the **backend** of the visualization platform; the **frontend** is [ZEN-explorer](https://github.com/ZEN-universe/ZEN-explorer).

[![PyPI - Version](https://img.shields.io/pypi/v/zen-temple?logo=pypi&logoColor=fff&color=0375b5)](https://pypi.org/project/zen-temple/)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fgithub.com%2FZEN-universe%2FZEN-temple%2Fraw%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)

[![GitHub Actions: Type checker](https://github.com/ZEN-universe/ZEN-temple/actions/workflows/run-mypy.yml/badge.svg)](https://github.com/ZEN-universe/ZEN-temple/actions/workflows/run-mypy.yml)

[![GitHub License](https://img.shields.io/github/license/ZEN-universe/ZEN-temple?label=License)](https://github.com/ZEN-universe/ZEN-temple/blob/main/LICENSE)

## 🧭 Which setup do I need?

The visualization platform is always **ZEN-temple (API) + ZEN-explorer (UI)**. A
released `zen-temple` package already bundles a built copy of ZEN-explorer, so
end users install a single package. When you work from a **checkout** of this
repository the frontend is _not_ included and has to be fetched once.

| Your goal                                          | Follow                                                                                                   | Clone                          | Extra tools |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------- |
| **Visualize my own ZEN-garden solutions**         | [Quick start](#-quick-start)                                                                            | nothing (install from PyPI)    | –           |
| **Develop ZEN-temple** (this repo)                | [Backend development](#-backend-development)                                                            | ZEN-temple                     | –           |
| **Develop ZEN-explorer** (the frontend)           | [ZEN-explorer README → Development](https://github.com/ZEN-universe/ZEN-explorer#-development)           | ZEN-explorer **and** ZEN-temple | Node.js     |

### Which shell / terminal?

Every command block below runs the same in **PowerShell**, **Windows Command
Prompt (`cmd`)** and **macOS/Linux `bash`/`zsh`**. `conda`, `pip`, `git` and the
`zen-*` commands behave identically in all of them. Where a step genuinely
differs between shells (copying `.env`, running a `bash` script) each variant is
shown and labelled.

## 🛠️ Requirements

- [Conda](https://docs.conda.io/en/latest/miniconda.html) (Miniconda is enough)
- Python 3.11 or higher
- Node.js with npm – only if you also develop ZEN-explorer

## 🚀 Quick start

Use this to visualize your own solutions. You do **not** need to clone this
repository.

```
conda create --name zen python==3.13
conda activate zen
pip install zen-garden zen-temple
```

Run ZEN-garden to produce an `outputs` folder (or use an existing one), then from
the directory that contains `outputs` start the platform:

```
zen-visualization
```

Your browser opens at <http://localhost:8000/explorer/>. Point ZEN-temple at a
different solutions folder with `zen-visualization --outputs-folder <path>`.

## 🐍 Backend development

Use this when you want to change ZEN-temple itself.

1. **Clone and enter the repository:**

   ```
   git clone https://github.com/ZEN-universe/ZEN-temple.git
   cd ZEN-temple
   ```

2. **Create the environment and install in editable mode:**

   ```
   conda create --name zen python==3.13
   conda activate zen
   pip install -e .[mypy]
   ```

3. **Fetch the ZEN-explorer frontend.** A checkout ships only a placeholder
   page, and `zen-visualization` refuses to start without the real build. 
   
   **Skip this step if you are developing ZEN-explorer in parallel** – run
     ZEN-temple with `--api-only` instead (see
     [Developing against a live ZEN-explorer](#developing-against-a-live-zen-explorer)).

   Pull a prebuilt copy from the latest published `zen-temple` release:

   ```
   zen-temple-fetch-explorer
   ```

   - Add `--version <x.y.z>` to match a specific `zen-temple` release.
   - The files land in `zen_temple/explorer/` and are git-ignored.


4. **Create your `.env` file** from the example:

   PowerShell:

   ```powershell
   Copy-Item .env.example .env
   ```

   Command Prompt (`cmd`):

   ```bat
   copy .env.example .env
   ```

   bash / zsh:

   ```bash
   cp .env.example .env
   ```

   `SOLUTION_FOLDER` in `.env` is only a fallback; the `-o/--outputs-folder`
   flag and the current working directory take precedence.

### Run the server

```
conda activate zen
zen-visualization --reload
```

By default ZEN-temple searches for solutions in `./outputs` and then in the
current working directory. To select a solution folder explicitly, use:

```
zen-visualization --outputs-folder <path-to-solutions>
```

The equivalent module invocation is `python -m zen_temple.main --reload`. For all
available command line arguments run:

```
python -m zen_temple.main --help
```

If the server refuses to start with a "port ... is not available" message, an
earlier `zen-visualization` is probably still running. Stop it, or pass
`--port <other-port>` (and set `PUBLIC_TEMPLE_URL` for the ZEN-explorer dev
server accordingly).

### Developing against a live ZEN-explorer

When you also run the ZEN-explorer dev server, start ZEN-temple in **API-only**
mode. The bundled frontend is then neither required nor served, so you can skip
`zen-temple-fetch-explorer`:

```
zen-visualization --api-only --no-open-browser --reload
```

Then follow [ZEN-explorer's README](https://github.com/ZEN-universe/ZEN-explorer#-development)
to start its dev server with `npm run dev`. The UI is served from
<http://localhost:5173/> and talks to this API at <http://localhost:8000/api/>.

## 📤 Release workflow

To create a new release of ZEN-temple follow the steps below. For each major
release (e.g. from `v0.4.x` to `v0.5.0`) the version numbers of ZEN-explorer and
ZEN-temple are kept in sync. The `scripts/bump_version.sh` helper must be run in
**bash** (Git Bash or WSL on Windows).

1. Bump version in ZEN-explorer `bash scripts/bump_version.sh` and update its CHANGELOG.md.
2. Commit and upload the updated files to GitHub.
3. Create a new release for ZEN-explorer:
   https://github.com/ZEN-universe/ZEN-explorer/releases/new
4. Bump version in ZEN-temple `bash scripts/bump_version.sh` and update [CHANGELOG.md](CHANGELOG.md).
5. Commit and upload the updated files to GitHub.
6. Create a new release for ZEN-temple, e.g. `<version>`. For a pre-release also add a suffix `.dev1`, i.e. `<version>.dev1`, and mark the release as pre-release:
   https://github.com/ZEN-universe/ZEN-temple/releases/new
7. (optional) Look at PyPI whether the new release has successfully been created:
   https://pypi.org/project/zen-temple/#history

## 🗂️ Folder structure

The folder and file structure is the following:

### Explorer

`explorer` contains the built ZEN-explorer frontend that ZEN-temple serves as
static files.

> [!WARNING]  
> Do not edit these files. They are produced by the ZEN-explorer build pipeline.
> In a checkout the folder only holds a placeholder page until you run
> `zen-temple-fetch-explorer` (or build ZEN-explorer yourself); the real files
> are git-ignored.

### Models

`models` contains the Pydantic-models that are used for the documentation. Some of these models also include generators that create an instance of the model given the path of a solution. See https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model

### Repositories

`repositories` contains the repositories for the data access. These provide an abstraction layer for the routers such that the data access is separated from the data source. Arguably, the generators defined in the models should be part of the repository in order to separate the instantiation of the models from the way that the solutions are stored. For more information visit https://www.umlboard.com/design-patterns/repository.html

### Routers

`routers` contains the FastAPI routers which define the different paths of the API server. For more information visit https://fastapi.tiangolo.com/tutorial/bigger-applications/

### Config

`config.py` contains the config of the application.

### Main

`main.py` contains the setup of the FastAPI application. For more information visit https://fastapi.tiangolo.com/tutorial/bigger-applications/
