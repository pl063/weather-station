
    async function getCurrentState (req, res) {
        try {
            const res = await Data.current_state.find();
            return res;
        } catch (err) {
            return false;
        }
    }

    
   module.exports = getCurrentState;