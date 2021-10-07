import './rankResult.scss';
import React from 'react';
import { Link, useParams } from 'react-router-dom';
import Marginer from '../../components/marginer';
import Recommend from '../../const/recomend';

export default function RankResult() {
  const { category } = useParams();
  console.log(category);

  return (
    <div className="ResultContainer">
      <Marginer direction="vertical" margin="2em" />
      <h1 style={{ display: 'flex' }}>
        <div style={{ color: '#ff5722' }}>{category}</div>을(를) 선택하셨습니다.
      </h1>
      <Marginer direction="vertical" margin="1em" />
      <h1>다음과 같은 음식점을 추천합니다.</h1>
      <Marginer direction="vertical" margin="4em" />

      <div className="RankResultContainer">
        {Recommend.map(option => (
          <button type="button" className="restaurantsChoice">
            <Marginer direction="vertical" margin="1em" />
            <h1 style={{ color: '#ff5722' }}>{option.name}</h1>
            <Marginer direction="vertical" margin="1em" />
            <h3>{option.address}</h3>
            <Marginer direction="vertical" margin="1em" />
            <h3>추천 메뉴 1. {option.menu1}</h3>
            <h3>추천 메뉴 2. {option.menu2}</h3>
            <h3>추천 메뉴 3. {option.menu3}</h3>
            <Marginer direction="vertical" margin="1em" />
            <div className="ratingContainer">
              <h3>종합 평점 :&nbsp;</h3>
              <h3 style={{ color: '#ff5722' }}>{option.rating}</h3>
            </div>
            <Marginer direction="vertical" margin="1em" />
          </button>
        ))}
      </div>
      <Marginer direction="vertical" margin="1em" />

      <Marginer direction="vertical" margin="4em" />
      <img alt="" className="ResultImage" />

      <div className="buttonContainer">
        <Marginer direction="vertical" margin="2em" />
        <Link to="/rank/">
          <button type="button" className="button-prev">
            이전
          </button>
        </Link>

        <Link to="/">
          <button type="button" className="button-next">
            홈으로
          </button>
        </Link>
      </div>
      <Marginer direction="vertical" margin="3em" />
    </div>
  );
}
