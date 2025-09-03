const fs = require('node:fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');
    const headers = lines[0].split(',');

    const firstnameIndex = headers.indexOf('firstname');
    const fieldIndex = headers.indexOf('field');

    const validLines = lines.slice(1).filter((line) => line.trim() !== '');
    const totalStudents = validLines.length;

    const studentsByField = {};

    validLines.forEach((line) => {
      const fields = line.split(',');
      const firstname = fields[firstnameIndex];
      const field = fields[fieldIndex];

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstname);
    });

    console.log(`Number of students: ${totalStudents}`);
    for (const [field, names] of Object.entries(studentsByField)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
