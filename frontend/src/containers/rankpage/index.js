import "./index.scss";
import React from "react";
import { Marginer } from "../../components/marginer";
import { RankContent } from "./rankContent";




export function RankPage(props) {

    return (

        <div className="PageContainer">

        <Marginer direction="vertical" margin="2em"/>

        <RankContent/>
        
        </div>

    );
}