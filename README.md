
# Automatic Programming tool

Powered by **gemini 1.5 flash** python script tool that makes possible to create software using AI. No human neeeded. Its possible due to gemini 1.5 context window size (1 millilon tokens).

Application works with Gemini Python API library and gives AI ability to: 
- List work folder and see all folders and files in directory, and subdirectories.
- Get content of file by its name
- Write content to file
- Insert content to file after specific line
- Replace specific line in file
Last two options was added to reduce AI context usage, so developing should be much cheaper, especially with large files, because AI dont need to rewrite all file content to make small changes.

But unforchantly its still not capable of full-scale programming, because Gemini 1.5 not smart enought to write good code
