<!--
SPDX-FileCopyrightText: 2026 Nahyun Park <nahowo@naver.com>

SPDX-License-Identifier: MIT
-->

# Final_Consonant_Formatter_CLI
A Simple CLI tool for Final_Consonant_Formatter.

### How to use
1. Install fc_formatter_cli
    ```
        $ pip install fc_formatter_cli
    ```
2. Use fc_formatter_cli
    ```
        $ fc-formatter-cli subject {noun} {verb}
        $ fc-formatter-cli object {noun} {verb}
    ```

### Example
```
    $ fc-formatter-cli subject 강아지 산책한다
    created sentence: 강아지가 산책한다

    $ fc-formatter-cli object 저녁 먹는다
    created sentence: 저녁을 먹는다
```
