export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDerpatments(allEmployees) {
      return Object.keys(allEmployees).length;
    },
  };
}
