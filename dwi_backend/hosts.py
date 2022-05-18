from django_hosts import patterns, host

host_patterns = patterns('',
                         host('dwi-api', 'dwi_backend.urls', name='dwi-api'),
                         )
