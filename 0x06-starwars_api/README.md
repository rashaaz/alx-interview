#!/usr/bin/env bash

cat <<EOF > README.md
# 0x06 Star Wars API

This project involves interacting with the Star Wars API to fetch and display information about characters from specific movies. The script provided allows you to retrieve and print the list of characters from a Star Wars movie based on the movie ID.

## Project Details

### Concepts Covered

- **HTTP Requests in JavaScript**:
  - Making HTTP requests using the \`request\` module or \`fetch\` in Node.js.
  
- **Working with APIs**:
  - Understanding RESTful APIs and parsing JSON data returned by them.

- **Asynchronous Programming**:
  - Managing asynchronous operations with callbacks, promises, and \`async/await\` syntax.
  
- **Command Line Arguments in Node.js**:
  - Accessing command-line arguments using \`process.argv\`.
  
- **Array Manipulation and Iteration**:
  - Iterating over arrays and manipulating data structures for formatting and displaying character names.

### Requirements

- **Node Version**: 10.14.x
- **Code Style**: Semi-standard compliant with semicolons.
- **Executable Files**: All files must be executable.
- **README.md**: Must include project details, usage instructions, and setup information.
  
### Usage

To run the script, use the following format in your terminal:

\`\`\`bash
./0-starwars_characters.js <Movie ID>
\`\`\`

Replace \`<Movie ID>\` with the ID of the Star Wars movie you want to fetch characters from.

### Installation

1. **Install Node 10:**
   \`\`\`bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   \`\`\`

2. **Install Semi-Standard:**
   \`\`\`bash
   sudo npm install semistandard --global
   \`\`\`

3. **Install Request Module:**
   \`\`\`bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   \`\`\`

### Example

\`\`\`bash
./0-starwars_characters.js 3
\`\`\`

Output:
\`\`\`
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
\`\`\`

EOF

