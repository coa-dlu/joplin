'''
    This is where you set environment variables that you want to set specifically for
    your PR branch only.
    The key is your git branch name.
    Within that branch name, set the environment vars that you'd like to override.
    Whatever you set in that object will not contaminate the environment vars of any other branch.
    You're allowed to override any environment var (even ones in vars_from_circleci),
    though you probably don't want to.
    branch_overrides are not required for every branch.
'''
branch_overrides = {
    "4340-official-documents": {
        "LOAD_DATA": "fixtures",
        "V3_WIP": True,
    },
    "master": {
        "LOAD_DATA": "fixtures",
        "V3_WIP": True,
    },
    "4266-guide": {
        "LOAD_DATA": "fixtures",
        "V3_WIP": True,
    },
    "import-everything": {
        "LOAD_DATA": "importer",
        "V3_WIP": True,
    },
    "4311-stream-block-error": {
        "LOAD_DATA": "fixtures",
        "V3_WIP": True,
    },
    "news-migration-test": {
        "LOAD_DATA": "",
    },
}
