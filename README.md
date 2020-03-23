# Starchive

Archive all your starred repositories locally.

##### Dependencies

- python3
    - art
    - GitPython
    - pygithub
    - python-gitlab
    - pyyaml

##### Usage

Define your local backup archiving directory under 'outputdir' in the config.yaml.

Define each user as follows.

```yaml
  000X:
    - 'username'
    - 'github/gitlab'
    - 'security token'
```

All repositories will update and clone into the archiving directory under the associated users name.
