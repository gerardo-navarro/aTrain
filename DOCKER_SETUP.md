# Docker Development Environment for aTrain

This guide explains how to set up and use the Docker development environment for aTrain.

## Prerequisites

- Docker (version 20.10 or higher)
- Docker Compose (version 2.0 or higher) or docker-compose (version 1.29 or higher)

## Quick Start

### Using Make (Recommended)

If you have `make` installed, you can use the provided Makefile for easier commands:

```bash
# Show all available commands
make help

# Build and start the development environment
make up

# Or start in detached mode (runs in background)
make up-d
```

### Using Docker Compose Directly

1. **Build and start the development environment:**

```bash
docker compose up --build
```

Or with older Docker Compose:
```bash
docker-compose up --build
```

2. **Access the application:**

Open your browser and navigate to:
```
http://localhost:5000
```

3. **Stop the development environment:**

Press `Ctrl+C` in the terminal, or run:
```bash
make down
# or
docker compose down
```

## Example Development Workflow

Here's a typical development session:

```bash
# 1. Start the development environment
make up

# The application is now running at http://localhost:5000
# Make changes to files in the aTrain/ directory

# 2. View logs in real-time (in another terminal)
make logs

# 3. Access the container shell if needed
make shell

# Inside the container, you can:
# - Run Python commands
# - Install additional packages
# - Debug issues

# 4. Initialize models if needed (first time setup)
make init-models

# 5. When done, stop the environment
make down

# 6. To clean up everything including volumes
make clean
```

## Development Workflow

### Using Make Commands

The Makefile provides convenient shortcuts:

```bash
make build          # Build the Docker image
make up             # Start the development environment
make up-d           # Start in detached mode (background)
make down           # Stop the development environment
make restart        # Restart the container
make logs           # View logs
make shell          # Open a bash shell in the container
make clean          # Remove containers, networks, and volumes
make init-models    # Initialize and download ML models
```

### Building the Container

If you make changes to dependencies in `pyproject.toml`, rebuild the container:

```bash
make build
# or
docker compose build
```

### Live Code Changes

The Docker setup mounts the `aTrain` directory as a volume, so any changes you make to the Python code will be automatically reflected in the running container (Flask will auto-reload).

### Running Commands Inside the Container

To execute commands inside the running container:

```bash
make shell
# or
docker compose exec atrain bash
```

Once inside, you can run Python commands, install packages, etc.

### Viewing Logs

To view application logs:

```bash
make logs
# or
docker compose logs -f atrain
```

## Common Development Tasks

### Testing Code Changes

1. Make changes to Python files in the `aTrain/` directory
2. Flask will automatically reload with your changes
3. Refresh your browser to see the updates

### Adding New Dependencies

1. Update `pyproject.toml` with new dependencies
2. Rebuild the container:
```bash
make build
make up
```

### Debugging

To debug the application:

```bash
# View real-time logs
make logs

# Or enter the container for interactive debugging
make shell

# Inside the container, you can use Python debugger
python -m pdb -m aTrain dev
```

### Running Python Scripts

To run custom Python scripts inside the container:

```bash
docker compose exec atrain python your_script.py
```

### Testing with Sample Data

Sample data is mounted at `/app/sample_data` inside the container. You can:

1. Add audio files to the `sample_data/` directory
2. Access them from the web interface
3. Test transcription functionality

## Model Management

Machine learning models are stored in a Docker volume named `atrain-models` to persist between container restarts.

To initialize and download required models:

```bash
make init-models
# or
docker compose exec atrain python -m aTrain init
```

Note: Model downloads may take significant time and disk space depending on which models are needed.

## Volume Management

### List volumes:
```bash
docker volume ls
```

### Remove model data (to start fresh):
```bash
docker compose down -v
```

**Warning:** This will delete all downloaded models.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, you can change it in `docker-compose.yml`:

```yaml
ports:
  - "5001:5000"  # Change 5001 to any available port
```

### Permission Issues

If you encounter permission issues with mounted volumes, you may need to adjust file ownership:

```bash
sudo chown -R $USER:$USER ./aTrain
```

### Container Fails to Start

Check the logs for error messages:

```bash
docker compose logs atrain
```

### Rebuilding from Scratch

To completely rebuild without cache:

```bash
docker compose build --no-cache
```

### SSL/Certificate Issues During Build

If you encounter SSL certificate verification errors during the Docker build process, this may be due to corporate proxies or network restrictions. You can:

1. Configure Docker to use your proxy settings:
```bash
# Create or edit ~/.docker/config.json
{
  "proxies": {
    "default": {
      "httpProxy": "http://proxy.example.com:8080",
      "httpsProxy": "http://proxy.example.com:8080"
    }
  }
}
```

2. Or use the local development setup instead (see below).

## GPU Support (Optional)

To enable NVIDIA GPU support for faster transcription:

1. Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

2. Modify `docker-compose.yml` to add GPU support:

```yaml
services:
  atrain:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

## Alternative: Local Development Setup

If Docker is not suitable for your environment, you can set up a local development environment:

### Prerequisites

- Python 3.10 or higher
- Git
- FFmpeg (for audio processing)
- (Optional) CUDA toolkit for GPU support

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/gerardo-navarro/aTrain.git
cd aTrain
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -e .
```

4. **Run in development mode:**
```bash
python -m aTrain dev
```

5. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

### Initializing Models (Local Setup)

```bash
python -m aTrain init
```

## Production Deployment

This Docker setup is designed for **development only**. For production deployment:

- Use a production-grade WSGI server (e.g., Gunicorn)
- Configure proper security settings
- Use environment-specific configuration
- Set up proper logging and monitoring
- Consider building standalone executables using PyInstaller

## Additional Resources

- [aTrain Manual Installation Guide](https://github.com/JuergenFleiss/aTrain/wiki/Manual-Installation-and-Builds#installation-for-developers-%EF%B8%8F)
- [aTrain Developer Wiki](https://github.com/JuergenFleiss/aTrain/wiki/Development:-Branching,-contributing-and-releases)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

## Architecture Notes

aTrain is designed as a desktop application using PyWebView to create a native window. In Docker development mode, it runs as a web application accessible via browser. The core functionality (transcription, speaker detection) remains the same in both modes.

## Quick Reference

### Essential Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make up` | Start development environment |
| `make down` | Stop development environment |
| `make logs` | View application logs |
| `make shell` | Access container shell |
| `make build` | Rebuild the Docker image |
| `make clean` | Remove all containers and volumes |
| `make init-models` | Download required ML models |

### File Locations (Inside Container)

| Path | Description |
|------|-------------|
| `/app/aTrain/` | Application source code (mounted) |
| `/app/sample_data/` | Sample audio files (mounted) |
| `/app/models/` | Downloaded ML models (persisted) |
| `/root/.cache/huggingface/` | Hugging Face model cache (persisted) |

### URLs

- Application: http://localhost:5000
- Change port in `docker-compose.yml` if needed
