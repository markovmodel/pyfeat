r"""

==============
Data container
==============

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import pytram as pt
import numpy as np

class Forge( pt.TRAMData ):
    """I am the data forge
    """
    def __init__( self, trajs, b_K_i=None, kT_K=None, kT_target=None, verbose=False ):
        super( Forge, self ).__init__( trajs, b_K_i=b_K_i, kT_K=kT_K, kT_target=kT_target, verbose=verbose )
        self._M_K_x = None
        self._b_IK_x = None

    @property
    def M_K_x( self ):
        if self._M_K_x is None:
            if self.verbose:
                print "# Copying Markov state sequences"
            self._M_K_x = np.zeros( shape=(self.n_therm_states,self.N_K.max()), dtype=np.intc )
            t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
            for traj in self.trajs:
                # SPEEDUP POSSIBLE!
                for t in xrange( traj['t'].shape[0] ):
                    K = traj['t'][t]
                    self._M_K_x[K,t_K[K]] = traj['m'][t]
                    t_K[K] += 1
            if self.verbose:
                print "# ... done"
        return self._M_K_x

    @property
    def b_IK_x( self ):
        if self._b_IK_x is None:
            if self.verbose:
                print "# Copying bias energy sequences"
            self._b_IK_x = np.zeros( shape=(self.n_therm_states,self.n_therm_states,self.N_K.max()), dtype=np.intc )
            if not self.kT_K is None:
                self.gen_b_IK_x_from_kT_K()
            else:
                self.gen_b_IK_x()
            if self.verbose:
                print "# ... done"
        return self._b_IK_x

    def gen_b_IK_x_from_kT_K( self ):
        t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
        for traj in self.trajs:
            # SPEEDUP POSSIBLE!
            for t in xrange( traj['t'].shape[0] ):
                K = traj['t'][t]
                for I in xrange( self.n_therm_states ):
                    self._b_IK_x[I,K,t_K[K]] = self.kT_K[K] * ( 1.0/self.kT_K[I] - 1.0/self.kT_K[self.kT_target] ) * traj['b'][t]
                t_K[K] += 1

    def gen_b_IK_x( self ):
        t_K = np.zeros( shape=(self.n_therm_states,), dtype=np.intc )
        for traj in self.trajs:
            if traj['u'].shape[1] == 1:
                raise pt.ExpressionError(
                        "b_IK_x",
                        "Trajectory with single energy columns detected - use kT file and kT target"
                    )
            if traj['u'].shape[1] != self.n_therm_states:
                raise pt.ExpressionError(
                        "b_IK_x",
                        "Trajectory with wrong number of energy columns detected (%d!=%d)" \
                        % ( traj['u'].shape[1], self.n_therm_states )
                    )
            # SPEEDUP POSSIBLE!
            for t in xrange( traj['t'].shape[0] ):
                K = traj['t'][t]
                for I in xrange( self.n_therm_states ):
                    self._b_IK_x[I,K,t_K[K]] = traj['b'][I,t]
                t_K[K] += 1





