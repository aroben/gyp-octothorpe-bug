{
  'targets': [
    {
      'target_name': 'test',
      'type': 'none',
      'sources': [
        'FileWith#.txt',
      ],
      'rules': [
        {
          'rule_name': 'text',
          'extension': 'txt',
          'outputs': [
            '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).txt',
          ],
          'action': [
            'cp',
            '<(RULE_INPUT_PATH)',
            '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).txt',
          ],
        },
      ],
    },
  ],
}
