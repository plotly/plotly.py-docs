:mod:`{{module}}`.{{objname}}
{{ underline }}==============

Hello this is my template

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :inherited-members: update_layout
   :members: update_layout, add_traces

   {% block methods %}
   .. automethod:: __init__
   .. automethod:: add_bar
   .. automethod:: update_layout
   .. automethod:: add_traces
   {% endblock %}


.. raw:: html

    <div class="clearer"></div>
