# Automation Tasks

This directory contains examples of automation scripts to help you learn how to use ChatGPT to automate repetitive tasks.

## Learning Objectives

- Learn to identify tasks that can be automated
- Practice using ChatGPT to generate automation scripts
- Understand how to customize generated code for your needs
- Develop skills in writing maintainable automation scripts

## Tasks

### Task 1: Batch File Renamer
**File**: `file_renamer.py`

A Python script that automates renaming multiple files by replacing patterns in filenames.

**Use Case**: Rename files like `test_file1.txt`, `test_file2.txt` to `prod_file1.txt`, `prod_file2.txt`

**Usage**:
```bash
./file_renamer.py <directory> <old_pattern> <new_pattern>
```

**How ChatGPT helped create this**:
- Prompt: "Write a Python script that renames all files in a directory by replacing a pattern"
- ChatGPT can help add features like:
  - Dry-run mode (preview changes without executing)
  - Regex pattern matching
  - Recursive directory processing
  - Undo functionality

### Task 2: Log Analyzer
**File**: `log_analyzer.py`

A Python script that analyzes log files and generates statistics.

**Use Case**: Quickly analyze application logs to find errors, warnings, and common IP addresses

**Usage**:
```bash
./log_analyzer.py <log_file>
```

**How ChatGPT helped create this**:
- Prompt: "Create a Python script to analyze log files and count errors, warnings, and extract IP addresses"
- ChatGPT can help extend with:
  - Time-based filtering
  - Custom log format parsing
  - Graphical reports
  - Email notifications for critical errors

### Task 3: Project Backup Script
**File**: `backup_project.sh`

A bash script that creates timestamped backups of projects while excluding unnecessary files.

**Use Case**: Automated project backups with cleanup of old backups

**Usage**:
```bash
./backup_project.sh [project_dir] [backup_dir]
```

**How ChatGPT helped create this**:
- Prompt: "Write a bash script to backup a project directory, excluding node_modules and .git"
- ChatGPT can help add:
  - Compression options
  - Remote backup support
  - Scheduled execution (cron)
  - Backup verification

## Creating Your Own Automation Scripts with ChatGPT

### Step 1: Identify the Task
Think about repetitive tasks you do regularly:
- File operations (rename, move, copy)
- Data processing (CSV manipulation, JSON parsing)
- System administration (backups, cleanups, monitoring)
- Development tasks (code formatting, documentation generation)

### Step 2: Describe to ChatGPT
Be specific about what you need:
- Input: What data/files you're working with
- Process: What transformations or operations to perform
- Output: What the result should look like
- Edge cases: Error handling requirements

### Step 3: Iterate and Improve
- Test the initial script
- Ask ChatGPT to add features or fix issues
- Request explanations for parts you don't understand
- Optimize for your specific use case

## Example ChatGPT Prompts for Automation

1. **File Management**:
   - "Write a Python script to organize files by extension into separate folders"
   - "Create a bash script to find and delete files older than 30 days"

2. **Data Processing**:
   - "Generate a Python script to convert CSV files to JSON format"
   - "Write a script to extract specific columns from multiple CSV files and combine them"

3. **Development**:
   - "Create a script to automatically update copyright years in all source files"
   - "Write a tool to generate boilerplate code for new Python modules"

4. **System Tasks**:
   - "Build a monitoring script that checks disk space and sends alerts"
   - "Create an automated deployment script for a web application"

## Best Practices

1. **Start Simple**: Begin with basic functionality, then add features
2. **Add Error Handling**: Always handle potential errors gracefully
3. **Make it Configurable**: Use command-line arguments or config files
4. **Document Your Code**: Add comments and usage instructions
5. **Test Thoroughly**: Test with various inputs before using in production
6. **Version Control**: Keep your automation scripts in git

## Tips for Better Automation with ChatGPT

- Explain the broader context of what you're trying to achieve
- Provide examples of input and desired output
- Ask for explanations of the code to learn as you automate
- Request best practices and potential improvements
- Iterate: Start with a basic version and enhance incrementally
