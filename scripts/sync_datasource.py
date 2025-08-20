# from extras.jobs import Job
from extras.scripts import Script
from core.models import DataSource

class SyncDataSourceJob(Script):
    class Meta:
        name = "Sync Data Source"
        description = "Manually sync a specific data source"
        has_sensitive_variables = False

    def run(self, data, commit):
        self.log_info("Starting data source sync...")

        # Get the data source by name or ID
        try:
            datasource = DataSource.objects.get(name="test-netbox-scripts")
            datasource.sync() #Uncomment this to sync datasource.
            self.log_success(f"Successfully synced data source: {datasource.name}")
        except DataSource.DoesNotExist:
            self.log_failure(f"Data source 'test-netbox-scripts' not found.")
