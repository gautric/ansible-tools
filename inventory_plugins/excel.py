from ansible.plugins.inventory import BaseInventoryPlugin

ANSIBLE_METADATA = {
    'metadata_version': '0.9.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: excel
plugin_type: inventory
short_description: Excel Inventory

options:
    excel_file:
        description: Excel file to use
        default: inventory.xlsx
        required: false
        type: str
    excel_groups:
        description: add inventory to this group
        default: all
        required: false
        type: str
author:
    - Greg I/O
'''

class InventoryModule(BaseInventoryPlugin):
    """Excel Inventory."""

    NAME = 'excel'

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
        # this method will parse 'common format' inventory sources and
        # update any options declared in DOCUMENTATION as needed
        config = self._read_config_data(path)

        excel_file = self.get_option('excel_file')
        excel_groups = self.get_option('excel_groups').split(",")

        [self.inventory.add_group(i) for i in excel_groups]

        my_list = [
            {"name":"my-name","description":"my Description"},
            {"name":"mon-name","description":"ma Description"},
            {"name":"meine name","description":"meine description"}
        ]

        [self.inventory.set_variable(i,"my-list",my_list) for i in excel_groups]



  