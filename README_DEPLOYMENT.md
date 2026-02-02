# Flask Application Deployment Guide

## Development vs Production

**Development Server (Current Setup)**
```bash
python Sow.py
```
- Single-threaded, not secure
- Debug mode enabled
- Suitable only for local development

**Production Server (Recommended)**

## Installation

1. **Install Gunicorn** (WSGI server):
```bash
pip install gunicorn
```

## Running with Gunicorn

### Basic Command:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

**Parameters:**
- `-w 4`: 4 worker processes (adjust based on your CPU cores)
- `-b 0.0.0.0:8000`: Bind to all interfaces on port 8000
- `wsgi:app`: Reference to the WSGI app (module:application)

### Using Configuration File:
```bash
gunicorn -c gunicorn_config.py wsgi:app
```

## Configuration Details

The `gunicorn_config.py` file includes:
- **workers**: Number of concurrent request handlers
- **timeout**: Request timeout (60 seconds)
- **max_requests**: Worker restart threshold
- **logging**: Access and error logs

## Important Notes

1. **Disable Debug Mode in Production**
   - Edit `Sow.py` and change `app.run(debug=True)` to `app.run(debug=False)`
   - Or set environment variable: `set FLASK_ENV=production`

2. **Use a Reverse Proxy**
   - Deploy behind Nginx or Apache in production
   - Nginx configuration example:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
       }
   }
   ```

3. **Environment Variables**
   - Use `.env` file for sensitive configuration
   - Set `FLASK_ENV=production`

4. **Monitoring & Process Management**
   - Consider using Supervisor or systemd to manage the Gunicorn process
   - Monitor logs in `logs/` directory

## Example Windows Task Scheduler Setup

For Windows deployment, you can schedule Gunicorn to start on boot:
1. Create a batch file `start_app.bat`:
```batch
cd C:\Users\Sowndharraj M\OneDrive\Documents\SOWNDHAR REPOSE\Flask_Learning
env\Scripts\gunicorn -c gunicorn_config.py wsgi:app
```

2. Add to Windows Task Scheduler to run on startup

## Performance Tuning

Adjust `workers` in `gunicorn_config.py`:
- Single core: 2-4 workers
- Quad core: 9-11 workers (2-4x CPU cores + 1)
- Formula: `(2 × CPU cores) + 1`
