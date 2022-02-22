{
  'targets': [
  {
    'target_name': 'nanomsg',
    'type': 'static_library',
    'includes': [ 'common.gypi' ],
    'conditions': [
      ['OS=="mac"', {
        'includes': [ 'macosx.gypi' ]
      }],
      ['OS=="linux"', {
        'includes': [ 'linux.gypi' ]
      }],
      ['OS=="win"', {
        'includes': [ 'win.gypi' ]
      }],
    ],
    'dependencies': ['nanomsg_download'],
  },
  {
    'target_name': 'nanomsg_download',
      "actions": [
        {
            "action_name": "download_nmsg",
            "inputs": [],
            "outputs": ["nanomsg-1.1.0.tar.gz"],
            "action": ["curl", "-L", "https://github.com/nanomsg/nanomsg/archive/refs/tags/1.1.0.tar.gz", "-o", "nanomsg-1.1.0.tar.gz"],
        },
        {
            "action_name": "mkdir_nanomsg",
            "inputs": [],
            "outputs": ["nanomsg"],
            "action": ["mkdir", "-p", "nanomsg"],
        },
        {
            "action_name": "extract_nmsg",
            "inputs": ["nanomsg-1.1.0.tar.gz", "nanomsg"],
            "outputs": ["nanomsg/src"],
            "action": ["tar", "--strip-components=1", "-xz", "-C", "nanomsg", "-f", "nanomsg-1.1.0.tar.gz"],
        },
    ],
  },
  ]
}