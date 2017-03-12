from os import environ as env
token = env['TOGGL_TOKEN']
gen_url = lambda s, e: 'https://%s:api_token@toggl.com/api/v8/time_entries?start_date=%s&end_date=%s' % (token,s,e)

days = [datetime(2017, 3, 11) + timedelta(days=-d) for d in range(14)]
ranges = [(d.isoformat()+'Z', (d+timedelta(days=1)).isoformat()+'Z') for d in days]
urls = [gen_url(s, e) for s, e in ranges]

entries = [rq.get(url, verify=False).json() for url in urls]
minimal = [{'start':e['start'], 'stop':e['stop'], 'pid': e['pid']} for e in sum(entries, [])]
