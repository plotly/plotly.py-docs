:mod:`{{module}}`.{{objname}}
{{ underline }}==============


.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   .. automethod:: __init__
   .. automethod:: show
   .. automethod:: update_layout
   .. automethod:: add_traces
   {% endblock %}

Other methods
{{ underline }}==============

.. autosummary::
   :toctree: generated/
   
   plotly.graph_objects.{{ objname }}


.. raw:: html

    <div class="clearer"></div>
