from ansible.plugins.inventory import BaseInventoryPlugin

ANSIBLE_METADATA = {
    'metadata_version': '0.9.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: example_hosts
plugin_type: inventory
short_description: An example Ansible Inventory Plugin
description:
    - "A very simple Inventory Plugin created for demonstration purposes only."
options:
author:
    - Greg I/O
'''

class InventoryModule(BaseInventoryPlugin):
    """An example inventory plugin."""

    NAME = 'example_hosts'

    def verify_file(self, path):
        """Verify that the source file can be processed correctly.

        Parameters:
            path:AnyStr The path to the file that needs to be verified

        Returns:
            bool True if the file is valid, else False
        """
        # Unused, always return True
        return True


    def parse(self, inventory, loader, path, cache):
        """Parse and populate the inventory with data about hosts.

        Parameters:
            inventory The inventory to populate

        We ignore the other parameters in the future signature, as we will
        not use them.

        Returns:
            None
        """
        super(InventoryModule, self).parse(inventory, loader, path)
        
        self.inventory.add_host("my-host")
        self.inventory.add_host("my-host-v2")

        self.inventory.set_variable("my-host", "ansible_connection", "local")     
        self.inventory.set_variable("my-host", "user", "my-user")
        
        self.inventory.set_variable("my-host-v2", "user1", "my-user")
        self.inventory.set_variable("my-host-v2", "user2", "my-user")

        self.inventory.add_group("mon-group")

        my_list = [
            {"name":"my-name","description":"my Description"},
            {"name":"mon-name","description":"ma Description"},
            {"name":"meine name","description":"meine description"}
        ]

        self.inventory.set_variable("mon-group","my-list",my_list)
        self.inventory.set_variable("mon-group","my-scalar-int",42)
        self.inventory.set_variable("mon-group","my-scalar-string","one value")


  