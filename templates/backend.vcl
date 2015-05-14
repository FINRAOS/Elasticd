{% for ip in resources %}
    web loop.index0 {
        host:{{ ip }}
    }
{% endfor %}
