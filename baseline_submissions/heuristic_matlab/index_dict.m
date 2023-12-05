classdef index_dict
    properties
        times
        indices
        AD_dex
        modes
    end
    
    methods
        function obj = index_dict()
            obj.times = obj.IDADIK();
            obj.indices = [];
            obj.AD_dex = [];
            obj.modes = obj.mode();
        end
    end
    
    methods (Static)
        function result = IDADIK()
            result.ID = [];
            result.AD = [];
            result.IK = [];
        end

        function result = mode()
            result.SK = [];
            result.end = [];
        end
    end
end
