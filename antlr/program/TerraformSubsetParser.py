# Generated from TerraformSubset.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,3,8,76,8,8,1,9,1,9,1,9,5,9,81,8,9,10,9,12,9,84,9,9,1,9,0,
        0,10,0,2,4,6,8,10,12,14,16,18,0,0,86,0,24,1,0,0,0,2,33,1,0,0,0,4,
        35,1,0,0,0,6,41,1,0,0,0,8,48,1,0,0,0,10,54,1,0,0,0,12,64,1,0,0,0,
        14,67,1,0,0,0,16,75,1,0,0,0,18,77,1,0,0,0,20,23,3,2,1,0,21,23,5,
        13,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,
        25,1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,
        0,29,34,3,4,2,0,30,34,3,6,3,0,31,34,3,8,4,0,32,34,3,10,5,0,33,29,
        1,0,0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,
        36,5,1,0,0,36,37,5,11,0,0,37,38,5,2,0,0,38,39,3,12,6,0,39,40,5,3,
        0,0,40,5,1,0,0,0,41,42,5,4,0,0,42,43,5,11,0,0,43,44,5,11,0,0,44,
        45,5,2,0,0,45,46,3,12,6,0,46,47,5,3,0,0,47,7,1,0,0,0,48,49,5,5,0,
        0,49,50,5,11,0,0,50,51,5,2,0,0,51,52,3,12,6,0,52,53,5,3,0,0,53,9,
        1,0,0,0,54,55,5,6,0,0,55,56,5,11,0,0,56,57,5,2,0,0,57,58,3,12,6,
        0,58,59,5,3,0,0,59,11,1,0,0,0,60,63,3,14,7,0,61,63,5,13,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,13,1,0,0,0,66,64,1,0,0,0,67,68,5,12,0,0,68,69,5,7,0,0,69,70,3,
        16,8,0,70,15,1,0,0,0,71,76,5,11,0,0,72,76,5,10,0,0,73,76,5,9,0,0,
        74,76,3,18,9,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,
        0,0,0,76,17,1,0,0,0,77,82,5,12,0,0,78,79,5,8,0,0,79,81,5,12,0,0,
        80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,19,1,
        0,0,0,84,82,1,0,0,0,7,22,24,33,62,64,75,82
    ]

class TerraformSubsetParser ( Parser ):

    grammarFileName = "TerraformSubset.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'provider'", "'{'", "'}'", "'resource'", 
                     "'variable'", "'output'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOLEAN", "NUMBER", "STRING", "IDENTIFIER", 
                      "COMMENT", "WS" ]

    RULE_terraform = 0
    RULE_block = 1
    RULE_provider = 2
    RULE_resource = 3
    RULE_variable = 4
    RULE_output = 5
    RULE_body = 6
    RULE_keyValue = 7
    RULE_expr = 8
    RULE_reference = 9

    ruleNames =  [ "terraform", "block", "provider", "resource", "variable", 
                   "output", "body", "keyValue", "expr", "reference" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BOOLEAN=9
    NUMBER=10
    STRING=11
    IDENTIFIER=12
    COMMENT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TerraformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TerraformSubsetParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.BlockContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.BlockContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.COMMENT)
            else:
                return self.getToken(TerraformSubsetParser.COMMENT, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_terraform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerraform" ):
                listener.enterTerraform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerraform" ):
                listener.exitTerraform(self)




    def terraform(self):

        localctx = TerraformSubsetParser.TerraformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_terraform)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8306) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 5, 6]:
                    self.state = 20
                    self.block()
                    pass
                elif token in [13]:
                    self.state = 21
                    self.match(TerraformSubsetParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(TerraformSubsetParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def provider(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ProviderContext,0)


        def resource(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ResourceContext,0)


        def variable(self):
            return self.getTypedRuleContext(TerraformSubsetParser.VariableContext,0)


        def output(self):
            return self.getTypedRuleContext(TerraformSubsetParser.OutputContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = TerraformSubsetParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.provider()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.resource()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.variable()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.output()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProviderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_provider

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProvider" ):
                listener.enterProvider(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProvider" ):
                listener.exitProvider(self)




    def provider(self):

        localctx = TerraformSubsetParser.ProviderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_provider)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(TerraformSubsetParser.T__0)
            self.state = 36
            self.match(TerraformSubsetParser.STRING)
            self.state = 37
            self.match(TerraformSubsetParser.T__1)
            self.state = 38
            self.body()
            self.state = 39
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.STRING)
            else:
                return self.getToken(TerraformSubsetParser.STRING, i)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)




    def resource(self):

        localctx = TerraformSubsetParser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(TerraformSubsetParser.T__3)
            self.state = 42
            self.match(TerraformSubsetParser.STRING)
            self.state = 43
            self.match(TerraformSubsetParser.STRING)
            self.state = 44
            self.match(TerraformSubsetParser.T__1)
            self.state = 45
            self.body()
            self.state = 46
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = TerraformSubsetParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(TerraformSubsetParser.T__4)
            self.state = 49
            self.match(TerraformSubsetParser.STRING)
            self.state = 50
            self.match(TerraformSubsetParser.T__1)
            self.state = 51
            self.body()
            self.state = 52
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformSubsetParser.BodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = TerraformSubsetParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(TerraformSubsetParser.T__5)
            self.state = 55
            self.match(TerraformSubsetParser.STRING)
            self.state = 56
            self.match(TerraformSubsetParser.T__1)
            self.state = 57
            self.body()
            self.state = 58
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValueContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValueContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.COMMENT)
            else:
                return self.getToken(TerraformSubsetParser.COMMENT, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = TerraformSubsetParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 60
                    self.keyValue()
                    pass
                elif token in [13]:
                    self.state = 61
                    self.match(TerraformSubsetParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ExprContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_keyValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValue" ):
                listener.enterKeyValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValue" ):
                listener.exitKeyValue(self)




    def keyValue(self):

        localctx = TerraformSubsetParser.KeyValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_keyValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 68
            self.match(TerraformSubsetParser.T__6)
            self.state = 69
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(TerraformSubsetParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(TerraformSubsetParser.BOOLEAN, 0)

        def reference(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ReferenceContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TerraformSubsetParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(TerraformSubsetParser.STRING)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(TerraformSubsetParser.NUMBER)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(TerraformSubsetParser.BOOLEAN)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.reference()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.IDENTIFIER)
            else:
                return self.getToken(TerraformSubsetParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)




    def reference(self):

        localctx = TerraformSubsetParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 78
                self.match(TerraformSubsetParser.T__7)
                self.state = 79
                self.match(TerraformSubsetParser.IDENTIFIER)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





