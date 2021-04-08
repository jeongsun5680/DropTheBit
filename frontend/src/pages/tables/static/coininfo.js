import React, { Component } from "react";

class CoinInfo extends Component {
  render() {
    // var { id, name_kr, name_en } = this.state.props;
    var lists = [
      {
        id: "BTC",
        name_kr: "비트코인",
        name_en: "Bitcoin",
        standard: {
          market: "Upbit",
          market_KRW: 77777777,
          market_USD: 66666.32,
        },
        target: {
          market: "Binance",
          market_KRW: 66666666,
          market_USD: 5555500,
          diff_KRW: 11111111,
          diff_USD: 1111132,
          diff_percent: 1442,
        },
      },
      {
        id: "ETH",
        name_kr: "이더리움",
        name_en: "Etherem",
        standard: {
          market: "Upbit",
          market_KRW: 11111,
          market_USD: 6666623232323.32,
        },
        target: {
          market: "Binance",
          market_KRW: 62226666666,
          market_USD: 55551233500,
          diff_KRW: 1111111211,
          diff_USD: 1111122323323,
          diff_percent: 14422222222,
        },
      },
    ];
    return (
      <tbody>
        {lists.map((row) => (
          <tr>
            <td>1</td>
            <td>
              <img
                src={"https://static.upbit.com/logos/" + row.id + ".png"}
                alt={row.id}
                title={row.id}
                height="16"
              ></img>
              <span class="text-muted fw-semi-bold">{row.id}</span>
            </td>
            <td>
              <span class="text-muted fw-semi-bold">
                {row.name_kr}({row.name_en})
              </span>
            </td>
            <td>{row.standard.market_KRW} 원</td>
            <td>{row.target.market_KRW} 원</td>
            <td>
              {row.target.diff_KRW} ({row.target.diff_percent}%)
            </td>
          </tr>
        ))}
      </tbody>
    );
  }
}

export default CoinInfo;
