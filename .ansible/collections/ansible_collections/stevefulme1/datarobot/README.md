> **EXPERIMENTAL** - This collection is a proof of concept and is not production ready.
> Modules may use placeholder API endpoints and have not been validated against real infrastructure.
> Do not use in production environments.

        # stevefulme1.datarobot

        Ansible Collection for **DataRobot**.

        ## Modules

        - `stevefulme1.datarobot.project` -- Manage DataRobot projects
- `stevefulme1.datarobot.project_info` -- List or retrieve DataRobot projects
- `stevefulme1.datarobot.model` -- Manage DataRobot models
- `stevefulme1.datarobot.model_info` -- List or retrieve DataRobot models
- `stevefulme1.datarobot.deployment` -- Manage DataRobot deployments
- `stevefulme1.datarobot.deployment_info` -- List or retrieve DataRobot deployments
- `stevefulme1.datarobot.prediction_server` -- Manage DataRobot prediction servers
- `stevefulme1.datarobot.prediction_server_info` -- List or retrieve DataRobot prediction servers
- `stevefulme1.datarobot.data_source` -- Manage DataRobot data sources
- `stevefulme1.datarobot.data_source_info` -- List or retrieve DataRobot data sources
- `stevefulme1.datarobot.feature_list` -- Manage DataRobot feature lists
- `stevefulme1.datarobot.feature_list_info` -- List or retrieve DataRobot feature lists
- `stevefulme1.datarobot.use_case` -- Manage DataRobot use cases
- `stevefulme1.datarobot.use_case_info` -- List or retrieve DataRobot use cases
- `stevefulme1.datarobot.monitoring_job` -- Manage DataRobot monitoring jobs
- `stevefulme1.datarobot.monitoring_job_info` -- List or retrieve DataRobot monitoring jobs

        ## Roles

        - `datarobot_setup` -- Set up DataRobot platform configuration
- `model_deploy` -- Deploy models to DataRobot prediction servers
- `model_monitor` -- Configure DataRobot model monitoring

        ## EDA Event Source

        - `stevefulme1.datarobot.datarobot_events` -- Poll DataRobot for events

        ## Requirements

        - Python >= 3.9
        - `requests` library
        - ansible-core >= 2.16

        ## Installation

        ```bash
        ansible-galaxy collection install stevefulme1.datarobot
        ```

        ## License

        GPL-3.0-or-later
