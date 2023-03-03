import * as React from 'react';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import SearchIcon from '@mui/icons-material/Search';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';

import { makeStyles } from '@mui/styles';
import axios from 'axios';


import {
  apiCalled,
  setData,
} from "../redux/reducers/Counter/counter.actions"
import { connect } from 'react-redux';
import { CircularProgress } from '@mui/material';
const useStyles = makeStyles(theme => ({
  paper: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
    verticalAlign: "middle",
    boxShadow: "4px 4px 4px rgba(0, 0, 0, 0.25)",
    borderRadius: "25px",
  }
}))



export function CustomizedInputBase(props) {
  const [input, setInput] = React.useState('');
  const [subgraph, setSubgraph] = React.useState('');

  const Search = async (event) => {
    event.preventDefault();
    console.log(input)
    props.apiCalled(true)

    const res = await axios.post('http://127.0.0.1:5000/api/v1/dashboard', {
      input: input,
      subgraph: subgraph,
    })



    const persons = res.data;
    // props.setData([{"decimals":9,"id":"0xcf0c122c6b73ff809c693db761e7baebe62b6a2e","name":"FLOKI","symbol":"FLOKI","transferCount":"274254"},{"decimals":18,"id":"0x320623b8e4ff03373931769a31fc52a4e78b5d70","name":"Reserve Rights","symbol":"RSR","transferCount":"121409"},{"decimals":18,"id":"0xc5102fe9359fd9a28f877a67e36b0f050d81a3cc","name":"Hop","symbol":"HOP","transferCount":"78497"},{"decimals":18,"id":"0xa2cd3d43c775978a96bdbf12d733d5a1ed94fb18","name":"Chain","symbol":"XCN","transferCount":"70327"},{"decimals":9,"id":"0xa67e9f021b9d208f7e3365b2a155e3c55b27de71","name":"KleeKai","symbol":"KLEE","transferCount":"37061"}]);
    props.setData(res.data);

    props.apiCalled(false)
    console.log(persons)


    // navigate('/')
  }
  //   const classes = useStyles()
  const handleChange = (event) => {

    setSubgraph(event.target.value);
  };

  return (
    <Paper
      sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 410 }}
    >
      <FormControl sx={{ p: '10px' }} aria-label="search">
        <InputLabel id="demo-simple-select-label">SubGraph</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={subgraph}
          label="SubGraph"
          onChange={handleChange}
        >
          <MenuItem value={"aave-governance"}>aave-governance</MenuItem>
          <MenuItem value={"uniswap-v3"}>uniswap-v3</MenuItem>
          <MenuItem value={"opensea-v2"}>opensea-v2</MenuItem>
          <MenuItem value={"uniswap-governance"}>uniswap-governance</MenuItem>
        </Select>
      </FormControl>

      <Box
        component="form"
        sx={{
          '& > :not(style)': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
        onSubmit={Search}
      >
        <TextField
          id="outlined-controlled"
          label="Enter Prompt"
          value={input}
          onChange={(event) => {
            setInput(event.target.value);
          }}
        />
      </Box>

      <IconButton type="submit" sx={{ p: '10px' }} aria-label="search">
        <SearchIcon onClick={(e) => { Search(e) }} />
      </IconButton>


    </Paper>
  );
}

const mapStateToProps = state => {
  return {
    count: state.counter.count,
    data: state.counter.data
  }
}

const mapDispatchToProps = dispatch => {
  return {
    setData: (data) => dispatch(setData(data)),
    apiCalled: (data) => dispatch(apiCalled(data))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(CustomizedInputBase)
