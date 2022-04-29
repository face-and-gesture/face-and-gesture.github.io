// Libraries
//   Bootstrap (Style Framework)
{% include js/lib/jquery-3.5.1.min.js %}
{% include js/lib/popper.min.js %}
{% include js/lib/bootstrap.js %}

//   FontAwesome (Icons)
//     Imported via CSS and webfonts

// Conference
window.conference = {
    config: {
        baseurl: '{{ site.conference.baseurl }}'
    }
};


// Program
{% include js/lib/syncscroll.js %}
{% include js/program.js %}

// Leaflet (Map Display)
{% include partials/get_enable_map.html %}
{% if enable_map %}
    {% include js/lib/leaflet.js %}
    {% include js/lib/leaflet-easybutton.js %}
    {% include js/lib/leaflet-locatecontrol.js %}
    {% include js/lib/leaflet-providers.js %}

    {% include js/map.js %}
{% endif %}

// Modals ("Popups")
{% include js/modal.js %}

// Live and Streaming
{% if site.conference.live %}
    {% include js/live.js %}
{% endif %}

// Load configuration and start initialization
{% include js/init.js %}
