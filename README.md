# Shell-VCR

Shell-VCR is a tool to intercept, record and replay shell commands.
This can be used to convert integration tests into unit tests, by
intercepting shell commands and replaying their prerecorded outputs,
kept in git next to you tests.

Create a bin folder with a symlink for each binary you want to
intercept and point it to this binary.

Record executables by running your commands like this:
`PATH=./vcr-bin/:$PATH VCR_MODE=RECORD VCR_REMOTE_HOST=someremote ./test.py`

After that you can run your tests like this:
`PATH=./vcr-bin/:$PATH VCR_MODE=REPLAY ./test.py`

TODO:
- Since the VCRs output is meant to be parsed by other programs,
  error handling and reporting is tricky.
- We should create command specific lock files during recording
  to make this thread / process save.
