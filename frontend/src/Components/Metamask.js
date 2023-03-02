import React, { Component } from 'react';
import { ethers } from "ethers";
import { Button } from '@mui/material';

import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  status: {
    danger: '#e53e3e',
  },
  palette: {
    primary: {
      main: '#f2ebeb',
      contrastText: '#515151',
      backgroundColor: "white"
    }
  },
});

class Metamask extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  async connectToMetamask() {
    const provider = new ethers.providers.Web3Provider(window.ethereum)
    const accounts = await provider.send("eth_requestAccounts", []);
    const balance = await provider.getBalance(accounts[0]);
    const balanceInEther = ethers.utils.formatEther(balance);
    this.setState({ selectedAddress: accounts[0], balance: balanceInEther })


    // <div>
        // <p>Welcome {this.state.selectedAddress}</p>
        // <p>Your ETH Balance is: {this.state.balance}</p>
        // </div>
  }
  renderMetamask() {
    if (!this.state.selectedAddress) {
      return (
        // <button onClick={() => this.connectToMetamask()}>Connect to Metamask</button>
        <Button color="primary"  onClick={() => this.connectToMetamask()} sx={[{ "&:hover": { backgroundColor: 'grey' , position: "sticky", top: 0, float: 'right'} }]}>Connect</Button>
      )
    } else {
      return (
        <Button variant="contained" sx={{ position: "sticky", top: 0}} color="success">
          Connected
        </Button>
      );

    }
  }

  render() {
    return(
      <div>
        <ThemeProvider theme={theme}>
        {this.renderMetamask()}
        </ThemeProvider>
      </div>
    )
  }
}

export default Metamask;