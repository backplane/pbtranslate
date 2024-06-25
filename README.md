# pbtranslate

Command-line utility which translates text in the clipboard.

## Usage

When invoked with `-h` or `--help` arguments, the program emits the following help text.

```
usage: pbtranslate [-h] [--log-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}]
                   [--log-dir LOG_DIR] [--ollama-url OLLAMA_URL]
                   [--ollama-model OLLAMA_MODEL] [--stdin | --no-stdin]
                   [--stdout | --no-stdout]
                   [--target-language TARGET_LANGUAGE]

utility for language translation in the clipboard

options:
  -h, --help            show this help message and exit
  --log-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}
                        how verbosely to log to the console (default: 'INFO')
  --log-dir LOG_DIR     directory in which to write log files (default: None)
  --ollama-url OLLAMA_URL
                        URL for the Ollama server (default:
                        'https://ollama.local/')
  --ollama-model OLLAMA_MODEL
                        name of the model to use on the ollama server
                        (default: 'llama3')
  --stdin, --no-stdin   read input text from the standard input, instead of
                        the clipboard (default: False)
  --stdout, --no-stdout
                        write output to the standard out, instead of the
                        clipboard (default: False)
  --target-language TARGET_LANGUAGE
                        language which the input text should be translated
                        into (default: 'English')
```
