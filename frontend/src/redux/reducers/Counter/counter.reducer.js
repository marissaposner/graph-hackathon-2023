import { INCREMENT, DECREMENT, SETDATA } from './counter.types';


const INITIAL_STATE = {

    count: 0,
    data: ""
};

const reducer = (state = INITIAL_STATE, action) => {

    switch (action.type) {

        case INCREMENT:

           return {

             ...state, 
             count: state.count + 1,

           };

        case SETDATA:

           return {

             ...state, 
             data: action.data,

           };

        case DECREMENT:

           return {
              ...state, count: state.count - 1,

           };

         default: return state;

    }

};

export default reducer;