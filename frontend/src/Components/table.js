import * as React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { connect } from 'react-redux';
import { CircularProgress } from '@mui/material';

function buildColumns(data){
    let column_header = Object.keys(data[0]);
    var columns = []

    for (var index = 0; index < column_header.length; index++)
    {
        // console.log(column_header[index]);
        columns.push({id: column_header[index], label: column_header[index], minWidth: 170, align: "right",format: (value) => value })
    }

    
    return columns
    
}

// function buildRows(data){
//     var rows = []

//     for (var index = 0; index < data.length; index++)
//     {
//         rows.push(Object.values(data[index]))
//     }
//     return rows
// }

const columns = [
  { id: 'name', label: 'Name', minWidth: 170 },
  { id: 'code', label: 'ISO\u00a0Code', minWidth: 100 },
  {
    id: 'population',
    label: 'Population',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'size',
    label: 'Size\u00a0(km\u00b2)',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'density',
    label: 'Density',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toFixed(2),
  },
];

function createData(name, code, population, size) {
  const density = population / size;
  return { name, code, population, size, density };
}


export  function StickyHeadTable(props) {
    
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
//   console.log(props.data);
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  let columns = props.data ? buildColumns(props?.data) : [];
  if(props.isLoading){
    return (
      <CircularProgress sx={{ align: 'center', marginTop:"10px",} }  color="secondary"/>
  )}
  else{
    let rows = props.data? props.data: []; 


  return (
    props.data && (
    <Paper sx={{ width: '80%', overflow: 'hidden', align: 'center', marginTop:"10px"}}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.id}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  ));
}}

const mapStateToProps = state => {
    return {
      data: state.counter.data,
      isLoading: state.counter.isLoading
    }
  }

export default connect(mapStateToProps)(StickyHeadTable)