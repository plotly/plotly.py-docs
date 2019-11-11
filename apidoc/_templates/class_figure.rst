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

.. autoclass:: {{ objname }}
   :members:
   :inherited-members:

.. raw:: html

    <div class="clearer"></div>

