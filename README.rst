======================================
OpenERP Web 7.0 for OpenERP server 6.1
======================================

This addon adds a thin layer to make the Web addons 7.0 compatible
with server 6.1

There's no guarantee at all; it is only a proof of concept to experiment with
the new web client.

Instructions
------------

Install the various parts:

- lp:openobject-server/6.1
- lp:openobject-addons/6.1
- lp:openerp-web/7.0
- and this addon lp:~florent.x/openobject-addons/6.1-web_seven

Then launch the server with additional switch ``--load web_seven,web``.

Links
-----

* `Fork me on GitHub <https://github.com/florentx/openerpweb_seven>`_
