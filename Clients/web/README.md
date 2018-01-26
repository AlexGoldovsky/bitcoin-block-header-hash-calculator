# BlockHeaderHash Web Client

## running the http server
```
PYTHONPATH=. python Clients/web/index.py
```
or using nginx (also serves static files)
```
gunicorn --workers 50 --bind unix:bbhh.sock -m 000 wsgi
sudo nginx -c /path/to/repo/Clients/web/server.nginx
```

## Using The API
All API endpoints are registered under /api
example:
A GET request to `http://localhost/api/hash?version=3&pbh=0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6&mr=f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db&timestamp=1442663985&bits=403867578&nonce=3548193207`

__note:__ This assumes you're running this up on localhost

returns `{
  "hash": "00000000000000000be983a81043933c38008010b849fd6a35d5dd2d57f929bd"
}`

## TODO
- [ ] Handle Negative flow
- [ ] Use something sexier than jquery
- [ ] Add tests
- [ ] Add Dockerfile
- [ ] Preety response (Currently using alert)
- [ ] Add configurations
- [ ] Add logging
- [ ] nginx conf use environmet variables
- [ ] Add api explorer
  
