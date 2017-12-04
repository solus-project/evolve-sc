#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  This file is part of solus-sc
#
#  Copyright © 2014-2017 Ikey Doherty <ikey@solus-project.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#

from gi.repository import Gtk


class ScDetailsView(Gtk.Box):
    """ Shows details for a selected ProviderItem

        The details view is effectively the pretty view with all the relevant
        package/software details, screenshots, and actions to invoke removal,
        installation, etc.
    """

    __gtype_name__ = "ScDetailsView"

    context = None
    item = None

    # Header widgets
    header_name = None
    header_image = None
    header_summary = None

    # TODO: Make less dumb
    header_action = None

    def __init__(self, context):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        self.context = context

        self.build_header()
        self.show_all()

    def set_item(self, item):
        """ Update our UI for the current item """
        if item == self.item:
            return

        apps = self.context.appsystem
        id = item.get_id()

        self.header_name.set_markup(apps.get_name(id, item.get_name()))
        self.header_summary.set_markup(
            apps.get_summary(id, item.get_summary()))
        pbuf = apps.get_pixbuf_only(id)
        self.header_image.set_from_pixbuf(pbuf)
        print("got updated")

    def build_header(self):
        """ Build our main header area """
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        box.set_border_width(20)
        ebox = Gtk.EventBox()
        ebox.add(box)
        ebox.get_style_context().add_class("details-header")
        self.pack_start(ebox, False, False, 0)

        self.header_name = Gtk.Label("")
        self.header_name.get_style_context().add_class("huge-label")
        self.header_image = Gtk.Image()
        self.header_image.set_margin_end(24)
        self.header_image.set_margin_start(12)

        box.pack_start(self.header_image, False, False, 0)

        details_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.pack_start(details_box, True, True, 0)

        # name
        self.header_name.set_halign(Gtk.Align.START)
        self.header_name.set_halign(Gtk.Align.START)
        details_box.pack_start(self.header_name, True, True, 0)

        # summary
        self.header_summary = Gtk.Label("")
        self.header_summary.set_margin_top(6)
        self.header_summary.set_margin_bottom(6)
        self.header_summary.set_halign(Gtk.Align.START)
        details_box.pack_start(self.header_summary, False, False, 0)

        # actions
        self.header_action = Gtk.Button("Install")
        self.header_action.set_valign(Gtk.Align.CENTER)
        box.pack_end(self.header_action, False, False, 0)