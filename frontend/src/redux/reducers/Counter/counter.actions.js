import { INCREMENT, DECREMENT, SETDATA } from './counter.types';


export const increaseCounter = () => {

    return {

        type: INCREMENT,

    };

};

export const decreaseCounter = () => {

    return {

       type: DECREMENT,

    };

};

export const setData = (data) => {

    return {

        type: SETDATA,
        data: data

    };

};