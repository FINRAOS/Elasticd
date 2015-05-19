{#
Default VCL for web configs.

Expected Result:
    backend web1 {
        .host = "10.0.0.1"
        .port = "80"
    }
    backend web2 {
        .host = "10.0.0.1"
        .port = "80"
    }
    ...

Available Variables:
    (array) resources containing one or more (Resource) resource.
    Resource class and it's descendants will always implement __str__ to make it easier to use here.
#}


{% for ipresource in resources %}
    backend web{{ loop.index0 }} {
            .host = "{{ ipresource }}";
            .port = "80";
    }
{% endfor %}
