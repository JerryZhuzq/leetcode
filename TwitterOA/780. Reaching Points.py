class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx == tx and sy < ty and (sy - ty) % sx == 0:
            return True
        if sy == ty and sx < tx and (sx - tx) % sy == 0:
            return True

        return False

# simplest solution
        # while tx > sx and ty > sy:
        #     if tx > ty:
        #         tx %= ty
        #     else:
        #         ty %= tx
        # return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
        #        sy == ty and sx <= tx and (tx - sx) % sy == 0


# The fastest solution with tricks (not robust)
        # if tx == sx and ty == sy:
        #     return True
        # if tx % ty == 0:
        #     tx = ty
        #     if sy == ty and sx % sy == 0:
        #         return True
        # if ty % tx == 0:
        #     ty = tx
        #     if sx == tx and sy % sx == 0:
        #         return True
        # while(tx > 0 and ty > 0 and tx != ty):
        #     if tx > ty:
        #         if tx > 1000*ty:
        #             tx = tx % ty
        #         else:
        #             tx = tx - ty
        #     elif tx < ty:
        #         if ty > 1000*tx:
        #             ty = ty % tx
        #         else:
        #             ty = ty - tx
        #
        #     if sx == tx and sy == ty:
        #         return True
        # return False


#         if tx == sx and ty == sy:
#             return True

#         if tx == ty or tx < 1 or ty < 1:
#             return False

#         if tx > ty:
#             return self.reachingPoints(sx, sy, tx-ty, ty)
#         else:
#             return self.reachingPoints(sx, sy, tx, ty-tx)

#  recursive calls will generate too many iterations